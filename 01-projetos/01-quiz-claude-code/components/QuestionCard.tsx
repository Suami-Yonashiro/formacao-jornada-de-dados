"use client";

import type { Question } from "@/types";

interface QuestionCardProps {
  question: Question;
  onAnswer: (answer: boolean) => void;
  disabled?: boolean;
  selectedAnswer?: boolean | null;
}

const CATEGORY_LABEL: Record<string, string> = {
  fundamentos: "Fundamentos CLI",
  features: "Features e Produtividade",
  "api-sdk": "API / SDK",
  "boas-praticas": "Boas Práticas",
};

const DIFFICULTY_LABEL: Record<string, string> = {
  iniciante: "Iniciante",
  intermediario: "Intermediário",
  avancado: "Avançado",
};

export default function QuestionCard({
  question,
  onAnswer,
  disabled = false,
  selectedAnswer = null,
}: QuestionCardProps) {
  const getButtonStyle = (value: boolean) => {
    if (selectedAnswer === null) {
      return {
        backgroundColor: value ? "rgba(204,120,92,0.15)" : "rgba(255,255,255,0.04)",
        borderColor: value ? "rgba(204,120,92,0.5)" : "#404040",
        color: "#FAFAFA",
      };
    }
    if (selectedAnswer === value) {
      const wasCorrect = question.answer === value;
      return {
        backgroundColor: wasCorrect ? "rgba(74,222,128,0.15)" : "rgba(248,113,113,0.15)",
        borderColor: wasCorrect ? "#4ADE80" : "#F87171",
        color: wasCorrect ? "#4ADE80" : "#F87171",
      };
    }
    return {
      backgroundColor: "transparent",
      borderColor: "#2A2A2A",
      color: "#555",
    };
  };

  return (
    <div className="rounded-2xl p-6" style={{ backgroundColor: "#262626" }}>
      <div className="flex items-center gap-2 mb-4">
        <span
          className="text-xs font-medium px-2 py-0.5 rounded-full"
          style={{ backgroundColor: "rgba(204,120,92,0.15)", color: "#CC785C" }}
        >
          {CATEGORY_LABEL[question.category]}
        </span>
        <span className="text-xs" style={{ color: "#A3A3A3" }}>
          {DIFFICULTY_LABEL[question.difficulty]}
        </span>
      </div>

      <p className="text-lg font-medium leading-relaxed mb-8" style={{ color: "#FAFAFA" }}>
        {question.statement}
      </p>

      <div className="flex gap-3">
        {([true, false] as const).map((value) => (
          <button
            key={String(value)}
            onClick={() => onAnswer(value)}
            disabled={disabled}
            className="flex-1 py-4 rounded-xl border font-bold text-base transition-all duration-200 disabled:cursor-not-allowed"
            style={getButtonStyle(value)}
          >
            {value ? "Verdadeiro" : "Falso"}
          </button>
        ))}
      </div>
    </div>
  );
}
