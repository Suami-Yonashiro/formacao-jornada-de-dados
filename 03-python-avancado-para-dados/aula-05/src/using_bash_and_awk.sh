#!/usr/bin/env bash

# --- DOCUMENTAÇÃO DIDÁTICA --- 
# Script em Bash utilizando AWK e Pipe Viewer (pv)
# Objetivo: Processar dados streaming exibindo velocidade e progresso reais.

# 1. Validação do arquivo.
if [ ! -f data/measurements.txt ]; then
    echo "Erro: Arquivo data/measurements.txt não encontrado."
    exit 1
fi

# 2. Definição da quantidade de linhas (Padrão: 1 milhão).
if [ -z "$1" ]; then
    QTD=1000000
else
    QTD="$1"
fi

echo "Iniciando o pipeline. Processando $QTD linhas..."

# 3. O pipeline de execução com monitoramento visual
# Explicação das flags do pv:
#   -p: Mostra a barra de progresso (progress bar)
#   -e: Mostra o tempo estimado de término (eta)
#   -t: Mostra o tempo decorrido (tima)
#   -l: Conta por LINHAS em vez de contar por bytes
#   -s: Informa ao pv o tamanho total esperado ($QTD) para ele saber calcular a porcentagem.

head -n $QTD data/measurements.txt | pv -p -e -t -l -s $QTD | awk -F ";" '
{
	# Se a estação ainda não foi registrada, inicializa os limites
	if (!($1 in cnts)){
		mins[$1] = $2 
		maxs[$1] = $2 
	}
	else{
	    # Atualização lógica em tempo real
		if ($2 < mins[$1]) mins[$1] = $2
		if ($2 > maxs[$1]) maxs[$1] = $2
	}
	cnts[$1] += 1;
	sums[$1] += $2;
}
END {
    # Impressão final formatada
	for (v in cnts) {
	    printf "%s: %.1f/%.1f/%.1f\n", v, mins[v], (sums[v]/cnts[v]), max[v]
	}
}' | sort

echo "Processamento concluído!"