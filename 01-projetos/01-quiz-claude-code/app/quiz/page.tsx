"use client";

import { useQuiz, TOTAL, TIMER_DURATION } from "@/lib/useQuiz";
import ProgressBar from "@/components/ProgressBar";
import Timer from "@/components/Timer";
import QuestionCard from "@/components/QuestionCard";
import AnswerFeedback from "@/components/AnswerFeedback";
import ScoreBoard from "@/components/ScoreBoard";

function QuizSkeleton() {
  return (
    <div
      className="min-h-screen px-4 py-8 flex flex-col max-w-2xl mx-auto"
      style={{ backgroundColor: "#0F0F0F" }}
    >
      <div className="mb-5">
        <div className="flex justify-between mb-1.5">
          <div className="h-4 w-28 rounded-full animate-pulse" style={{ backgroundColor: "#262626" }} />
          <div className="h-4 w-8 rounded-full animate-pulse" style={{ backgroundColor: "#262626" }} />
        </div>
        <div className="h-1.5 rounded-full animate-pulse" style={{ backgroundColor: "#262626" }} />
      </div>

      <div className="mb-4 flex items-center gap-3">
        <div className="h-7 w-7 rounded-full animate-pulse" style={{ backgroundColor: "#262626" }} />
        <div className="flex-1 h-2 rounded-full animate-pulse" style={{ backgroundColor: "#262626" }} />
      </div>

      <div className="mb-5 flex gap-2">
        {[0, 1, 2].map((i) => (
          <div
            key={i}
            className="flex-1 h-16 rounded-xl animate-pulse"
            style={{ backgroundColor: "#1A1A1A" }}
          />
        ))}
      </div>

      <div className="rounded-2xl p-6 animate-pulse" style={{ backgroundColor: "#262626" }}>
        <div className="flex gap-2 mb-4">
          <div className="h-5 w-36 rounded-full" style={{ backgroundColor: "#333" }} />
          <div className="h-5 w-20 rounded-full" style={{ backgroundColor: "#333" }} />
        </div>
        <div className="h-5 rounded-full mb-2" style={{ backgroundColor: "#333" }} />
        <div className="h-5 w-4/5 rounded-full mb-8" style={{ backgroundColor: "#333" }} />
        <div className="flex gap-3">
          <div className="flex-1 h-14 rounded-xl" style={{ backgroundColor: "#333" }} />
          <div className="flex-1 h-14 rounded-xl" style={{ backgroundColor: "#333" }} />
        </div>
      </div>
    </div>
  );
}

export default function QuizPage() {
  const { state, answered, selectedAnswer, handleAnswer, handleExpire } = useQuiz();

  if (!state) return <QuizSkeleton />;

  const currentQuestion = state.questions[state.currentIndex];
  const questionNumber = state.currentIndex + 1;

  return (
    <div
      className="min-h-screen px-4 py-8 flex flex-col max-w-2xl mx-auto"
      style={{ backgroundColor: "#0F0F0F" }}
    >
      <div className="mb-5">
        <ProgressBar current={questionNumber} total={TOTAL} />
      </div>

      <div className="mb-4">
        <Timer
          key={state.currentIndex}
          duration={TIMER_DURATION}
          onExpire={handleExpire}
          paused={answered}
        />
      </div>

      <div className="mb-5">
        <ScoreBoard
          score={state.score}
          correctCount={state.correctCount}
          currentStreak={state.currentStreak}
          totalAnswered={answered ? questionNumber : state.currentIndex}
        />
      </div>

      <div className="flex flex-col gap-4 flex-1 justify-center">
        <QuestionCard
          question={currentQuestion}
          onAnswer={handleAnswer}
          disabled={answered}
          selectedAnswer={selectedAnswer}
        />

        {answered && (
          <AnswerFeedback
            correct={selectedAnswer !== null && selectedAnswer === currentQuestion.answer}
            correctAnswer={currentQuestion.answer}
            explanation={currentQuestion.explanation}
          />
        )}
      </div>
    </div>
  );
}
