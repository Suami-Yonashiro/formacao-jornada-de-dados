export type Category = "fundamentos" | "features" | "api-sdk" | "boas-praticas";
export type Difficulty = "iniciante" | "intermediario" | "avancado";

export interface Question {
  id: string;
  category: Category;
  difficulty: Difficulty;
  statement: string;
  answer: boolean;
  explanation: string;
}

export interface PlayerAnswer {
  questionId: string;
  correct: boolean;
  timeSpent: number;
}

export interface GameState {
  questions: Question[];
  currentIndex: number;
  score: number;
  correctCount: number;
  currentStreak: number;
  maxStreak: number;
  answers: PlayerAnswer[];
}

export interface ScoreEntry {
  id?: string;
  nickname: string;
  score: number;
  correct_count: number;
  created_at?: string;
}
