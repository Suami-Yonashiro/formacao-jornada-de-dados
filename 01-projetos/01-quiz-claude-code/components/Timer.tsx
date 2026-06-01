"use client";

import { useEffect, useRef, useState } from "react";

interface TimerProps {
  duration?: number;
  onExpire: () => void;
  paused?: boolean;
}

export default function Timer({ duration = 15, onExpire, paused = false }: TimerProps) {
  const [remaining, setRemaining] = useState(duration);
  const firedRef = useRef(false);

  useEffect(() => {
    setRemaining(duration);
    firedRef.current = false;
  }, [duration]);

  useEffect(() => {
    if (paused || remaining <= 0) return;

    const id = setTimeout(() => {
      setRemaining((prev) => {
        const next = prev - 1;
        if (next === 0 && !firedRef.current) {
          firedRef.current = true;
          onExpire();
        }
        return next;
      });
    }, 1000);

    return () => clearTimeout(id);
  }, [remaining, paused, onExpire]);

  const pct = (remaining / duration) * 100;
  const isWarning = remaining <= 5;
  const color = isWarning ? "#F87171" : "#CC785C";

  return (
    <div className="flex items-center gap-3">
      <span
        className="text-2xl font-bold tabular-nums w-7 text-right transition-colors duration-300"
        style={{ color }}
      >
        {remaining}
      </span>
      <div className="flex-1 h-2 rounded-full overflow-hidden" style={{ backgroundColor: "#262626" }}>
        <div
          className="h-full rounded-full transition-all duration-1000 ease-linear"
          style={{ width: `${pct}%`, backgroundColor: color }}
        />
      </div>
    </div>
  );
}
