"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { saveScore } from "@/lib/supabase";

interface QuizResult {
  score: number;
  correctCount: number;
  maxStreak: number;
}

interface StatCardProps {
  label: string;
  value: string;
  valueColor?: string;
}

function StatCard({ label, value, valueColor = "#FAFAFA" }: StatCardProps) {
  return (
    <div className="rounded-xl p-4 text-center" style={{ backgroundColor: "#1A1A1A" }}>
      <p className="text-xs mb-1" style={{ color: "#A3A3A3" }}>
        {label}
      </p>
      <p className="text-2xl font-bold tabular-nums" style={{ color: valueColor }}>
        {value}
      </p>
    </div>
  );
}

export default function ResultadoPage() {
  const router = useRouter();
  const [result, setResult] = useState<QuizResult | null>(null);
  const [nickname, setNickname] = useState("");
  const [saving, setSaving] = useState(false);
  const [saved, setSaved] = useState(false);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const raw = sessionStorage.getItem("quizResult");
    if (!raw) {
      router.replace("/");
      return;
    }
    // Fixes #1 e #2: try/catch + validação dos valores para evitar manipulação via DevTools
    try {
      const parsed = JSON.parse(raw);
      const MAX_SCORE = 4900; // máx real: 15×(100+75) + soma dos streak bonuses
      const score = Math.max(0, Math.min(Math.round(Number(parsed.score) || 0), MAX_SCORE));
      const correctCount = Math.max(0, Math.min(Math.round(Number(parsed.correctCount) || 0), 15));
      const maxStreak = Math.max(0, Math.min(Math.round(Number(parsed.maxStreak) || 0), 15));
      setResult({ score, correctCount, maxStreak });
    } catch {
      router.replace("/");
    }
  }, [router]);

  const handleSave = async () => {
    if (!result || saving || saved) return;
    setSaving(true);
    setError(null);
    try {
      await saveScore({
        nickname: nickname.trim() || "Anônimo",
        score: result.score,
        correct_count: result.correctCount,
      });
      setSaved(true);
      sessionStorage.removeItem("quizResult");
    } catch {
      setError("Não foi possível salvar. Verifique sua conexão e tente novamente.");
    } finally {
      setSaving(false);
    }
  };

  if (!result) return null;

  const percentage = Math.round((result.correctCount / 15) * 100);

  return (
    <div
      className="min-h-screen px-4 py-12 flex flex-col items-center justify-center max-w-md mx-auto"
      style={{ backgroundColor: "#0F0F0F" }}
    >
      <p className="text-xs font-semibold tracking-widest uppercase mb-2" style={{ color: "#CC785C" }}>
        Resultado
      </p>
      <h1 className="text-3xl font-bold mb-1" style={{ color: "#FAFAFA" }}>
        Quiz concluído!
      </h1>
      <p className="text-sm mb-8" style={{ color: "#A3A3A3" }}>
        Você acertou {result.correctCount} de 15 perguntas ({percentage}%)
      </p>

      <div className="w-full grid grid-cols-3 gap-3 mb-8">
        <StatCard
          label="Pontuação"
          value={result.score.toLocaleString("pt-BR")}
          valueColor="#CC785C"
        />
        <StatCard label="Acertos" value={`${result.correctCount}/15`} />
        <StatCard
          label="Melhor streak"
          value={String(result.maxStreak)}
          valueColor={result.maxStreak >= 3 ? "#4ADE80" : "#FAFAFA"}
        />
      </div>

      <div className="w-full rounded-2xl p-5 mb-6" style={{ backgroundColor: "#262626" }}>
        <h2 className="font-bold mb-3 text-sm" style={{ color: "#FAFAFA" }}>
          Salvar no Ranking Global
        </h2>
        <input
          type="text"
          placeholder="Seu nickname (opcional)"
          maxLength={30}
          value={nickname}
          onChange={(e) => setNickname(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && handleSave()}
          disabled={saved}
          className="w-full rounded-lg px-4 py-3 text-sm mb-3 outline-none border transition-colors"
          style={{
            backgroundColor: "#1A1A1A",
            color: "#FAFAFA",
            borderColor: "#404040",
          }}
        />
        {error && (
          <p className="text-xs mb-3" style={{ color: "#F87171" }}>
            {error}
          </p>
        )}
        <button
          onClick={handleSave}
          disabled={saving || saved}
          className="w-full py-3 rounded-lg font-bold text-sm transition-opacity disabled:opacity-60 disabled:cursor-not-allowed hover:opacity-90"
          style={{ backgroundColor: "#CC785C", color: "#FAFAFA" }}
        >
          {saved ? "Salvo com sucesso!" : saving ? "Salvando..." : "Salvar pontuação"}
        </button>
      </div>

      <div className="flex gap-3 w-full">
        <Link
          href="/quiz"
          className="flex-1 py-3 rounded-xl text-center font-bold text-sm border transition-colors hover:bg-white/5"
          style={{ borderColor: "#404040", color: "#FAFAFA" }}
        >
          Jogar novamente
        </Link>
        <Link
          href="/ranking"
          className="flex-1 py-3 rounded-xl text-center font-bold text-sm transition-colors hover:bg-white/5"
          style={{ backgroundColor: "#1A1A1A", color: "#A3A3A3" }}
        >
          Ver Ranking
        </Link>
      </div>
    </div>
  );
}
