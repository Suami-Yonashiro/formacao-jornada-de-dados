import { memo } from "react";

interface AnswerFeedbackProps {
  correct: boolean;
  correctAnswer: boolean;
  explanation: string;
}

const AnswerFeedback = memo(function AnswerFeedback({
  correct,
  correctAnswer,
  explanation,
}: AnswerFeedbackProps) {
  const borderColor = correct ? "#4ADE80" : "#F87171";
  const bgColor = correct ? "rgba(74,222,128,0.08)" : "rgba(248,113,113,0.08)";
  const label = correct ? "Correto!" : "Incorreto!";

  return (
    <div
      className="rounded-xl p-4 border transition-all duration-300"
      style={{ borderColor, backgroundColor: bgColor }}
    >
      <div className="flex items-center justify-between mb-2">
        <span className="font-bold text-base" style={{ color: borderColor }}>
          {label}
        </span>
        <span className="text-sm" style={{ color: "#A3A3A3" }}>
          Resposta certa:{" "}
          <span style={{ color: "#FAFAFA" }}>{correctAnswer ? "Verdadeiro" : "Falso"}</span>
        </span>
      </div>
      <p className="text-sm leading-relaxed" style={{ color: "#A3A3A3" }}>
        {explanation}
      </p>
    </div>
  );
});

export default AnswerFeedback;
