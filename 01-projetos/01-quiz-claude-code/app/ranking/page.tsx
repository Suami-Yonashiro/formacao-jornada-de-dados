import Link from "next/link";
import { fetchTopScores } from "@/lib/supabase";
import Leaderboard from "@/components/Leaderboard";
import type { ScoreEntry } from "@/types";

export const revalidate = 60; // refresh leaderboard every 60s

export default async function RankingPage() {
  let entries: ScoreEntry[] = [];

  try {
    entries = await fetchTopScores(50);
  } catch {
    // Supabase not configured or unreachable — show empty state
  }

  return (
    <div
      className="min-h-screen px-4 py-10 max-w-2xl mx-auto"
      style={{ backgroundColor: "#0F0F0F" }}
    >
      <div className="flex items-center justify-between mb-8">
        <div>
          <p
            className="text-xs font-semibold tracking-widest uppercase mb-1"
            style={{ color: "#CC785C" }}
          >
            Ranking
          </p>
          <h1 className="text-3xl font-bold" style={{ color: "#FAFAFA" }}>
            Top 50 Global
          </h1>
        </div>
        <Link
          href="/"
          className="text-sm transition-colors hover:opacity-70"
          style={{ color: "#A3A3A3" }}
        >
          ← Início
        </Link>
      </div>

      <div className="rounded-2xl p-6" style={{ backgroundColor: "#262626" }}>
        <Leaderboard entries={entries} />
      </div>

      <div className="mt-6 text-center">
        <Link
          href="/quiz"
          className="inline-block px-8 py-3 rounded-xl font-bold text-sm transition-opacity hover:opacity-90"
          style={{ backgroundColor: "#CC785C", color: "#FAFAFA" }}
        >
          Jogar agora
        </Link>
      </div>
    </div>
  );
}
