import { memo } from "react";

interface ScoreBoardProps {
  score: number;
  correctCount: number;
  currentStreak: number;
  totalAnswered: number;
}

interface StatProps {
  label: string;
  value: string | number;
  valueColor?: string;
}

function Stat({ label, value, valueColor = "#FAFAFA" }: StatProps) {
  return (
    <div className="flex-1 rounded-xl p-3 text-center" style={{ backgroundColor: "#1A1A1A" }}>
      <p className="text-xs mb-1" style={{ color: "#A3A3A3" }}>{label}</p>
      <p className="text-xl font-bold tabular-nums" style={{ color: valueColor }}>{value}</p>
    </div>
  );
}

const ScoreBoard = memo(function ScoreBoard({
  score,
  correctCount,
  currentStreak,
  totalAnswered,
}: ScoreBoardProps) {
  return (
    <div className="flex gap-2">
      <Stat label="Pontuação" value={score} valueColor="#CC785C" />
      <Stat label="Acertos" value={`${correctCount}/${totalAnswered}`} />
      <Stat
        label="Streak"
        value={currentStreak}
        valueColor={currentStreak >= 3 ? "#4ADE80" : "#FAFAFA"}
      />
    </div>
  );
});

export default ScoreBoard;
