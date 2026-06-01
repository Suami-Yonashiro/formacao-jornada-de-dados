import { createClient, type SupabaseClient } from "@supabase/supabase-js";
import type { ScoreEntry } from "@/types";

let _clientCache: SupabaseClient | null = null;

function getClient(): SupabaseClient {
  const url = process.env.NEXT_PUBLIC_SUPABASE_URL;
  const key = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY;
  if (!url || !key) throw new Error("Variáveis de ambiente do Supabase não configuradas.");
  // Fix #3: no servidor cada request recebe instância nova (evita estado compartilhado entre requests)
  if (typeof window === "undefined") return createClient(url, key);
  _clientCache ??= createClient(url, key);
  return _clientCache;
}

export async function saveScore(
  entry: Omit<ScoreEntry, "id" | "created_at">
): Promise<void> {
  const nickname = entry.nickname.trim().slice(0, 30) || "Anônimo";
  const { error } = await getClient().from("leaderboard").insert({
    nickname,
    score: entry.score,
    correct_count: entry.correct_count,
  });
  if (error) throw new Error(error.message);
}

export async function fetchTopScores(limit = 50): Promise<ScoreEntry[]> {
  const { data, error } = await getClient()
    .from("leaderboard")
    .select("id, nickname, score, correct_count, created_at")
    .order("score", { ascending: false })
    .limit(limit);
  if (error) throw new Error(error.message);
  return data ?? [];
}
