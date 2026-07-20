#!/usr/bin/env bash

# --- DOCUMENTAÇÃO DIDÁTICA ---
# Script em Bash adaptado para windows
# Objetivo: Medir o tempo de processamento em streaming sem dependências externas.

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

echo "Iniciando o pipeline. Processando $QTD linhas com AWK..."

# Captura o timestamp de início em nanosegundos.
START_TIME=$(date +%s.%N)

# 3. Pipeline corrigido: 'pv' removido para rodar nativamente no Windows.
head -n $QTD data/measurements.txt | awk -F ";" '
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
	    printf "%s: %.1f/%.1f/%.1f\n", v, mins[v], (sums[v]/cnts[v]), maxs[v]
	}
}' | sort

# Captura o timestamp de término
END_TIME=$(date +%s.%N)

# Calcula a diferença usando o utilitário 'awk' (já que o Bash não faz conta com decimais nativamente).
TEMPO_DECORRIDO=$(awk "BEGIN {print $END_TIME - $START_TIME}")

echo "----------------------------------------"
echo "Processamento concluído!"
printf "Bash/AWK levou: %.2f segundos\n" $TEMPO_DECORRIDO

# Resultados:
# 1 milhão 2.80 segundos
# 10 milhões 2.98 segundos
# 100 milhões 2.85 segundos
