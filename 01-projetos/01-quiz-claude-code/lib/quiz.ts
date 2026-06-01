import type { Question, Difficulty } from "@/types";

const QUESTIONS_PER_DIFFICULTY = 5;
const DIFFICULTIES: Difficulty[] = ["iniciante", "intermediario", "avancado"];

function shuffle<T>(arr: T[]): T[] {
  const copy = [...arr];
  for (let i = copy.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

export function selectQuestions(allQuestions: Question[]): Question[] {
  return DIFFICULTIES.flatMap((difficulty) => {
    const pool = allQuestions.filter((q) => q.difficulty === difficulty);
    return shuffle(pool).slice(0, QUESTIONS_PER_DIFFICULTY);
  });
}
