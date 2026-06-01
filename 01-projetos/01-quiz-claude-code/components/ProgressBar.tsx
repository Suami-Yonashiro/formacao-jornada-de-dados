import { memo } from "react";

interface ProgressBarProps {
  current: number;
  total: number;
}

const ProgressBar = memo(function ProgressBar({ current, total }: ProgressBarProps) {
  const pct = Math.min((current / total) * 100, 100);

  return (
    <div>
      <div className="flex justify-between text-sm mb-1.5" style={{ color: "#A3A3A3" }}>
        <span>Pergunta {current} de {total}</span>
        <span>{Math.round(pct)}%</span>
      </div>
      <div className="h-1.5 rounded-full overflow-hidden" style={{ backgroundColor: "#262626" }}>
        <div
          className="h-full rounded-full transition-all duration-500"
          style={{ width: `${pct}%`, backgroundColor: "#CC785C" }}
        />
      </div>
    </div>
  );
});

export default ProgressBar;
