import { useCallback, useEffect, useRef, useState } from "react";
import { useRouter } from "next/navigation";
import type { GameState, Question } from "@/types";
import questionsData from "@/data/questions.json";
import { selectQuestions } from "@/lib/quiz";
import { applyAnswer, initGameState } from "@/lib/scoring";

export const TOTAL = 15;
export const TIMER_DURATION = 15;
const FEEDBACK_MS = 2500;

export interface UseQuizReturn {
  state: GameState | null;
  answered: boolean;
  selectedAnswer: boolean | null;
  handleAnswer: (answer: boolean | null) => void;
  handleExpire: () => void;
}

export function useQuiz(): UseQuizReturn {
  const router = useRouter();
  const [state, setState] = useState<GameState | null>(null);
  const [answered, setAnswered] = useState(false);
  const [selectedAnswer, setSelectedAnswer] = useState<boolean | null>(null);

  const answeredRef = useRef(false);
  const startTimeRef = useRef<number>(Date.now());
  const stateRef = useRef<GameState | null>(null);
  // Assigned during render so handlers always see the latest state
  stateRef.current = state;

  useEffect(() => {
    const questions = selectQuestions(questionsData as Question[]);
    setState({ questions, ...initGameState() });
  }, []);

  // Primitive dependency avoids stale-closure issues with the full state object
  const currentIndex = state?.currentIndex ?? -1;
  useEffect(() => {
    if (currentIndex < 0) return;
    answeredRef.current = false;
    setAnswered(false);
    setSelectedAnswer(null);
    startTimeRef.current = Date.now();
  }, [currentIndex]);

  const advance = useCallback(
    (newState: GameState) => {
      const nextIndex = newState.currentIndex + 1;
      if (nextIndex >= TOTAL) {
        sessionStorage.setItem(
          "quizResult",
          JSON.stringify({
            score: newState.score,
            correctCount: newState.correctCount,
            maxStreak: newState.maxStreak,
          })
        );
        router.push("/resultado");
      } else {
        setState({ ...newState, currentIndex: nextIndex });
      }
    },
    [router]
  );

  const handleAnswer = useCallback(
    (answer: boolean | null) => {
      if (answeredRef.current || !stateRef.current) return;
      answeredRef.current = true;

      const current = stateRef.current;
      const secondsLeft =
        answer !== null
          ? Math.max(
              0,
              TIMER_DURATION - Math.floor((Date.now() - startTimeRef.current) / 1000)
            )
          : 0;
      const correct =
        answer !== null && answer === current.questions[current.currentIndex].answer;
      const timeSpent = TIMER_DURATION - secondsLeft;

      setAnswered(true);
      setSelectedAnswer(answer);

      const newState = applyAnswer(current, correct, timeSpent, secondsLeft);
      setState(newState);

      setTimeout(() => advance(newState), FEEDBACK_MS);
    },
    [advance]
  );

  const handleExpire = useCallback(() => handleAnswer(null), [handleAnswer]);

  return { state, answered, selectedAnswer, handleAnswer, handleExpire };
}
