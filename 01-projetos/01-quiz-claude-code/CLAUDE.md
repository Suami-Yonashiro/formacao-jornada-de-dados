# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A True/False quiz web app that educates developers about Claude Code through gamified gameplay with a global leaderboard. Full specification is in `prd.md`.

**Status:** Planning phase — Next.js project has not been initialized yet.

## Tech Stack

- **Framework:** Next.js (App Router) + TypeScript
- **Styling:** Tailwind CSS (dark mode default, Anthropic orange accent `#CC785C`)
- **Backend:** Supabase (PostgreSQL leaderboard, REST API, RLS enabled)
- **Deployment:** Vercel (auto-deploy on git push)
- **Questions:** Static `data/questions.json` (no database for content)

## Commands (once project is initialized)

```bash
npm install          # Install dependencies
npm run dev          # Dev server at http://localhost:3000
npm run build        # Production build
npm run lint         # ESLint
npx tsc --noEmit     # TypeScript type check
```

## Environment Variables

Required in `.env.local` (never commit):
```
NEXT_PUBLIC_SUPABASE_URL=...
NEXT_PUBLIC_SUPABASE_ANON_KEY=...
```

## Architecture

### Routing (App Router)
- `/` — Home: title, description, Start Quiz button, View Ranking link
- `/quiz` — Active gameplay: question card, timer, progress bar, answer feedback
- `/resultado` — Results: score, correct count, max streak, save-to-leaderboard form
- `/ranking` — Top 50 global leaderboard from Supabase

### Game Logic
- 15 questions per session: 5 beginner → 5 intermediate → 5 advanced (from `data/questions.json`)
- 15-second countdown timer per question; timeout = wrong answer (resets streak)
- Scoring: `base(100) + speedBonus(secondsLeft × 5) + streakBonus((streak-2) × 25 if streak ≥ 3)`
- Game state lives in React state on `/quiz`; passed to `/resultado` via URL params or session storage

### Key Types (`types/index.ts`)
```typescript
type Category = "fundamentos" | "features" | "api-sdk" | "boas-praticas"
type Difficulty = "iniciante" | "intermediario" | "avancado"

interface Question {
  id: string; category: Category; difficulty: Difficulty
  statement: string; answer: boolean; explanation: string
}

interface ScoreEntry {
  nickname: string; score: number; correct_count: number; created_at?: string
}
```

### Supabase `leaderboard` Table
```sql
create table leaderboard (
  id uuid primary key default gen_random_uuid(),
  nickname text not null default 'Anônimo',
  score integer not null,
  correct_count integer not null,
  created_at timestamptz not null default now()
);
-- RLS: public SELECT and INSERT only (no UPDATE/DELETE)
```

## Planned Folder Structure
```
app/
  page.tsx, quiz/page.tsx, resultado/page.tsx, ranking/page.tsx
  layout.tsx, globals.css
components/
  QuestionCard.tsx, Timer.tsx, AnswerFeedback.tsx
  ScoreBoard.tsx, ProgressBar.tsx, Leaderboard.tsx
lib/
  supabase.ts, scoring.ts, quiz.ts
data/
  questions.json       # 30–50 questions, all True/False
types/
  index.ts
```

## V1 Scope Boundaries

Out of scope (do not implement unless PRD is updated):
- User authentication (nickname only, no accounts)
- Non-True/False question formats
- Admin panel (edit questions via JSON file directly)
- Internationalization (Portuguese only)
- Native mobile app
