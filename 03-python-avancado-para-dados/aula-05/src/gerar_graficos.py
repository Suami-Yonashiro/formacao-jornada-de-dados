"""Gera os gráficos PNG de comparação de performance do desafio do bilhão de linhas.

Os tempos vêm dos comentários "# Resultados:" no final de cada script da pasta src/.
Rode com:  python src/gerar_graficos.py
Os PNGs são salvos em assets/.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

# --- Dados do benchmark (segundos) ------------------------------------------
# Ordem das colunas: 1 milhão, 10 milhões, 100 milhões de linhas
VOLUMES = ["1M", "10M", "100M"]
VOLUMES_NUM = [1_000_000, 10_000_000, 100_000_000]

# nome -> (cor, [tempos por volume])
RESULTADOS = {
    "Python puro": ("#9e9e9e", [0.88, 8.91, 197.24]),
    "Python + tqdm": ("#bdbdbd", [1.10, 12.39, 218.75]),
    "Pandas": ("#150458", [1.05, 3.84, 45.08]),
    "Dask": ("#fc6e6b", [0.55, 3.71, 32.50]),
    "Polars": ("#0b7285", [0.11, 0.64, 8.61]),
    "DuckDB": ("#f0a202", [0.55, 1.34, 7.20]),
    # Bash/AWK tem ressalva (head limita as linhas); incluído só onde faz sentido.
    "Bash + AWK": ("#4caf50", [2.80, 2.98, 2.85]),
}

ASSETS = Path(__file__).resolve().parent.parent / "assets"
ASSETS.mkdir(exist_ok=True)

# Estilo geral (tema escuro discreto, combina com material de slides)
plt.rcParams.update(
    {
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "font.size": 11,
        "axes.titlesize": 14,
        "axes.titleweight": "bold",
    }
)


def _valor_nas_barras(ax, bars, fmt="{:.2f}s", offset_frac=0.01):
    """Escreve o valor em cima de cada barra."""
    ymax = ax.get_ylim()[1]
    for bar in bars:
        h = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            h + ymax * offset_frac,
            fmt.format(h),
            ha="center",
            va="bottom",
            fontsize=8,
        )


# 1) Barras horizontais — foco em 100 milhões (a comparação "manchete") -------
def grafico_100m():
    dados = [
        (nome, cor, tempos[2])
        for nome, (cor, tempos) in RESULTADOS.items()
        if nome != "Bash + AWK"
    ]  # Bash fica de fora (benchmark não confiável em 100M)
    dados.sort(key=lambda x: x[2])
    nomes = [d[0] for d in dados]
    cores = [d[1] for d in dados]
    tempos = [d[2] for d in dados]

    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.barh(nomes, tempos, color=cores, edgecolor="#333", linewidth=0.6)
    ax.invert_yaxis()  # mais rápido no topo
    ax.set_xlabel("Tempo de processamento (segundos) — menor é melhor")
    ax.set_title("Desafio do Bilhão de Linhas — 100 milhões de linhas")
    for bar, t in zip(bars, tempos):
        ax.text(
            bar.get_width() + max(tempos) * 0.01,
            bar.get_y() + bar.get_height() / 2,
            f"{t:.2f}s",
            va="center",
            fontsize=9,
            fontweight="bold",
        )
    ax.set_xlim(0, max(tempos) * 1.12)
    ax.grid(axis="x", linestyle="--", alpha=0.4)
    fig.tight_layout()
    fig.savefig(ASSETS / "comparativo_100M.png", dpi=150)
    plt.close(fig)


# 2) Barras agrupadas nos 3 volumes (escala log) ------------------------------
def grafico_agrupado():
    nomes = [n for n in RESULTADOS if n != "Bash + AWK"]
    x = np.arange(len(VOLUMES))
    largura = 0.13

    fig, ax = plt.subplots(figsize=(11, 6))
    for i, nome in enumerate(nomes):
        cor, tempos = RESULTADOS[nome]
        offset = (i - (len(nomes) - 1) / 2) * largura
        ax.bar(
            x + offset,
            tempos,
            largura,
            label=nome,
            color=cor,
            edgecolor="#333",
            linewidth=0.5,
        )

    ax.set_yscale("log")
    ax.set_ylabel("Tempo (segundos) — escala logarítmica")
    ax.set_xlabel("Volume de dados (número de linhas)")
    ax.set_title("Tempo de processamento por ferramenta e volume de dados")
    ax.set_xticks(x)
    ax.set_xticklabels([f"{v} linhas" for v in VOLUMES])
    ax.legend(ncol=3, fontsize=9, loc="upper left")
    ax.grid(axis="y", which="both", linestyle="--", alpha=0.3)
    fig.tight_layout()
    fig.savefig(ASSETS / "comparativo_agrupado.png", dpi=150)
    plt.close(fig)


# 3) Escalabilidade — como cada ferramenta cresce (log-log) -------------------
def grafico_escalabilidade():
    fig, ax = plt.subplots(figsize=(10, 6))
    for nome, (cor, tempos) in RESULTADOS.items():
        estilo = "--" if nome == "Bash + AWK" else "-"
        ax.plot(
            VOLUMES_NUM,
            tempos,
            marker="o",
            label=nome,
            color=cor,
            linewidth=2,
            linestyle=estilo,
        )

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("Número de linhas (escala log)")
    ax.set_ylabel("Tempo em segundos (escala log)")
    ax.set_title("Escalabilidade: como o tempo cresce com o volume")
    ax.set_xticks(VOLUMES_NUM)
    ax.get_xaxis().set_major_formatter(
        mticker.FuncFormatter(
            lambda v, _: {1e6: "1M", 1e7: "10M", 1e8: "100M"}.get(v, v)
        )
    )
    ax.legend(fontsize=9)
    ax.grid(which="both", linestyle="--", alpha=0.3)
    fig.text(
        0.5,
        0.01,
        "Bash + AWK (tracejado): tempo ~constante porque o 'head -n' limitou as linhas lidas — benchmark não confiável em 10M/100M.",
        ha="center",
        fontsize=8,
        style="italic",
        color="#555",
    )
    fig.tight_layout(rect=[0, 0.03, 1, 1])
    fig.savefig(ASSETS / "escalabilidade.png", dpi=150)
    plt.close(fig)


# 4) Speedup relativo ao Python puro em 100M ----------------------------------
def grafico_speedup():
    base = RESULTADOS["Python puro"][1][2]  # 197.24s
    dados = [
        (nome, cor, base / tempos[2])
        for nome, (cor, tempos) in RESULTADOS.items()
        if nome not in ("Python puro", "Bash + AWK")
    ]
    dados.sort(key=lambda x: x[2])
    nomes = [d[0] for d in dados]
    cores = [d[1] for d in dados]
    speed = [d[2] for d in dados]

    fig, ax = plt.subplots(figsize=(9, 5))
    bars = ax.barh(nomes, speed, color=cores, edgecolor="#333", linewidth=0.6)
    ax.set_xlabel("Quantas vezes mais rápido que o Python puro (100M de linhas)")
    ax.set_title("Ganho de performance vs. Python puro")
    for bar, s in zip(bars, speed):
        ax.text(
            bar.get_width() + max(speed) * 0.01,
            bar.get_y() + bar.get_height() / 2,
            f"{s:.1f}x",
            va="center",
            fontsize=9,
            fontweight="bold",
        )
    ax.set_xlim(0, max(speed) * 1.12)
    ax.grid(axis="x", linestyle="--", alpha=0.4)
    fig.tight_layout()
    fig.savefig(ASSETS / "speedup_vs_python.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    grafico_100m()
    grafico_agrupado()
    grafico_escalabilidade()
    grafico_speedup()
    print(f"Gráficos salvos em: {ASSETS}")
    for png in sorted(ASSETS.glob("*.png")):
        print(" -", png.name)
