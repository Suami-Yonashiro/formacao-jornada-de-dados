import type { ScoreEntry } from "@/types";

interface LeaderboardProps {
  entries: ScoreEntry[];
}

function formatDate(dateStr: string): string {
  return new Date(dateStr).toLocaleDateString("pt-BR", {
    day: "2-digit",
    month: "2-digit",
    year: "2-digit",
  });
}

function RankBadge({ rank }: { rank: number }) {
  const colors: Record<number, string> = {
    1: "#FFD700",
    2: "#C0C0C0",
    3: "#CD7F32",
  };
  const color = colors[rank] ?? "#A3A3A3";
  return (
    <span className="font-bold tabular-nums" style={{ color }}>
      {rank}
    </span>
  );
}

export default function Leaderboard({ entries }: LeaderboardProps) {
  if (entries.length === 0) {
    return (
      <p className="text-center py-12" style={{ color: "#A3A3A3" }}>
        Nenhuma pontuação registrada ainda. Seja o primeiro!
      </p>
    );
  }

  return (
    <div className="overflow-x-auto">
      <table className="w-full text-sm">
        <thead>
          <tr className="text-left text-xs uppercase tracking-wide" style={{ color: "#A3A3A3" }}>
            <th className="pb-3 pr-4 w-10">#</th>
            <th className="pb-3 pr-4">Nickname</th>
            <th className="pb-3 pr-4 text-right">Pontuação</th>
            <th className="pb-3 pr-4 text-right">Acertos</th>
            <th className="pb-3 text-right">Data</th>
          </tr>
        </thead>
        <tbody>
          {entries.map((entry, i) => {
            const rank = i + 1;
            const isTop3 = rank <= 3;
            return (
              <tr
                key={entry.id ?? i}
                className="border-t"
                style={{ borderColor: "#2A2A2A" }}
              >
                <td className="py-3 pr-4">
                  <RankBadge rank={rank} />
                </td>
                <td
                  className="py-3 pr-4 font-medium"
                  style={{ color: isTop3 ? "#FAFAFA" : "#D4D4D4" }}
                >
                  {entry.nickname}
                </td>
                <td className="py-3 pr-4 text-right font-bold tabular-nums" style={{ color: "#CC785C" }}>
                  {entry.score.toLocaleString("pt-BR")}
                </td>
                <td className="py-3 pr-4 text-right tabular-nums" style={{ color: "#A3A3A3" }}>
                  {entry.correct_count}/15
                </td>
                <td className="py-3 text-right" style={{ color: "#555" }}>
                  {entry.created_at ? formatDate(entry.created_at) : "—"}
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}
