# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Leia primeiro o `CLAUDE.md` da raiz do repositório (`../../CLAUDE.md`) — profiles, catálogo,
armadilhas do workspace e o contrato de dados valem aqui sem repetição. Este arquivo cobre só o
que é específico da Noite 2.

## O que é esta pasta

Noite 2 da Imersão: silver, gold, pipeline e testes, construídos ao vivo como um Databricks
Asset Bundle (DABs) em seis prompts / seis deploys — ver `README.md` para o roteiro completo
(passo a passo de setup, os seis prompts, números esperados, armadilhas medidas contra o
workspace). Não repita esse conteúdo aqui; leia o README quando for executar algo desta noite.

## Estado atual do bundle `rotaperfume/`

`rotaperfume/` é hoje a saída **crua** de `databricks bundle init default-python` — nomeado
`my_project` internamente (`databricks.yml`, `src/my_project/`, `src/my_project_etl/`,
`sample_job.job.yml`), catálogo `workspace` e host ainda de template. Isso é esperado: é o
ponto de partida do **Prompt 1**, não um bundle quebrado. Cada um dos seis prompts do README
estende este mesmo bundle — não recrie do zero, e não trate os nomes `my_project`/`taxis.py`/
`sample_trips` como bug a corrigir isoladamente: eles somem quando o Prompt 1 for aplicado.

Os prompts referenciam uma pasta `prd/` (com `prd/CLAUDE.md`, `prd/prompt-0N-*.md`,
`prd/00-reset.sh`) que **ainda não existe** neste checkout — é material a criar/colar ao vivo
durante a aula. `.llm/prompt_01.md` é um rascunho anterior do Prompt 1 e já diverge do README
publicado num ponto importante: usa o profile `projeto-dados-ia` e o host
`dbc-84cd5511-fa25.cloud.databricks.com`, enquanto o README usa `jornada` como profile sugerido.
**Nunca escolha um desses dois por conta própria** — pergunte ao usuário qual profile e host
valem para a execução atual (regra da raiz: nunca deixe o profile implícito).

## Dataset (`dados/`)

`dados/erp/` (produtos, pedidos, itens_pedido, pagamentos, estoque) e `dados/crm/` (clientes,
vendedores, carteira, oportunidades, visitas) — os 10 CSVs gerados por
`material/gerar_dataset.py --saida ./dados --seed 42`, referenciados pelo caminho relativo
`aulas/aula-02-engenharia-de-dados/dados/` a partir da raiz do repo. Não versionado no root
`.gitignore`, mas presente neste checkout — não regenere nem edite: a seed 42 é o que garante
que todo aluno chega ao mesmo número (ver números de conferência no README).

## Comandos usados nesta pasta

Executados de dentro de `rotaperfume/`, sempre com `--target dev` (default) e `--profile`
explícito:

```bash
databricks bundle validate --target dev --profile <perfil>
databricks bundle deploy   --target dev --profile <perfil>
databricks bundle run rotaperfume_pipeline --target dev --profile <perfil>
databricks bundle summary  --target dev --profile <perfil>   # links do job/dashboard/Genie
```

O catálogo (`scripts/criar-catalogo.sh`, ainda a criar no Prompt 1) roda **antes** do primeiro
deploy — no Free Edition, com Default Storage ligado, a API do Unity Catalog não cria catálogo
(`Metastore storage root URL does not exist`); só `CREATE CATALOG` via SQL funciona. O upload do
raw (`scripts/subir-raw.sh`) roda **depois** do deploy, porque depende do Volume já existir.

## Convenção ao adicionar as seis camadas de prompt

Cada prompt no README amplia o mesmo job (`rotaperfume_pipeline`) e o mesmo `databricks.yml` —
raw (1 tarefa) → bronze → silver ×4 → gold (dimensões/fato/marts/testes) → dashboard → views de
negócio/Genie. Ao implementar um prompt, confira o número de conferência da tabela do README
correspondente (ex.: silver.clientes = 3.000, `SUM(valor_liquido)` = R$ 102.303.828,05) — se o
número não bater, é sinal de dado descartado sem querer, não de flutuação aceitável.
