import type { GameState, PlayerAnswer } from "@/types";

export function calcStreakBonus(streak: number): number {
  return streak >= 3 ? (streak - 2) * 25 : 0;
}

export function calcPoints(secondsLeft: number, streak: number): number {
  return 100 + secondsLeft * 5 + calcStreakBonus(streak);
}

export function applyAnswer(
  state: GameState,
  correct: boolean,
  timeSpent: number,
  secondsLeft: number
): GameState {
  const currentQuestion = state.questions[state.currentIndex];
  const newStreak = correct ? state.currentStreak + 1 : 0;
  const pointsEarned = correct ? calcPoints(secondsLeft, newStreak) : 0;

  const answer: PlayerAnswer = {
    questionId: currentQuestion.id,
    correct,
    timeSpent,
  };

  return {
    ...state,
    score: state.score + pointsEarned,
    correctCount: state.correctCount + (correct ? 1 : 0),
    currentStreak: newStreak,
    maxStreak: Math.max(state.maxStreak, newStreak),
    answers: [...state.answers, answer],
  };
}

export function initGameState(): Omit<GameState, "questions"> {
  return {
    currentIndex: 0,
    score: 0,
    correctCount: 0,
    currentStreak: 0,
    maxStreak: 0,
    answers: [],
  };
}
