# PRD — Quiz Web: "Domine o Claude Code"

> Documento de Requisitos de Produto (Product Requirements Document)
> Versão 1.0 · Data: 2026-06-01
> Status: Aprovado para desenvolvimento

---

## 1. Visão Geral

### 1.1. Resumo executivo
Um **quiz web de Verdadeiro ou Falso** sobre o **Claude Code**, cobrindo desde conceitos introdutórios (negócio/fundamentos) até tópicos avançados (API/SDK, features de produtividade). O objetivo é educar e engajar a comunidade de desenvolvedores de forma gamificada, reforçando o aprendizado sobre a ferramenta.

### 1.2. Problema / Oportunidade
- Há crescente interesse no Claude Code, mas o conhecimento é fragmentado (docs, blogs, vídeos).
- Falta um recurso **interativo e divertido** que valide e fixe o conhecimento.
- Oportunidade de criar um conteúdo educacional viral, fácil de compartilhar, com ranking competitivo.

### 1.3. Objetivos (Business Goals)
| Objetivo | Métrica de sucesso |
|---|---|
| Engajar a comunidade | Nº de partidas concluídas |
| Educar sobre Claude Code | Taxa de acerto média por categoria |
| Estimular competição | Nº de entradas no leaderboard |
| Compartilhamento | Partidas iniciadas via link compartilhado |

### 1.4. Público-alvo
- **Iniciantes**: curiosos sobre o que é Claude Code, como instalar e usar.
- **Intermediários**: desenvolvedores que já usam e querem testar conhecimento sobre features.
- **Avançados**: usuários de API/SDK, automações, hooks e MCP.

### 1.5. Não-objetivos (Out of Scope — V1)
- Autenticação de usuários / contas (apenas nickname no leaderboard).
- Múltiplos formatos de pergunta (apenas Verdadeiro/Falso).
- Painel administrativo (perguntas editadas direto no JSON).
- Internacionalização (V1 em **português**).
- App mobile nativo (apenas web responsivo).

---

## 2. Escopo Funcional

### 2.1. Fluxo principal do usuário
1. **Tela inicial (Home)** — título, breve descrição, botão "Iniciar Quiz", link "Ver Ranking".
2. **Partida** — 15 perguntas em dificuldade progressiva, timer de 15s por pergunta.
3. **Feedback por pergunta** — acerto/erro imediato; em caso de erro (ou sempre), exibir a resposta correta + explicação.
4. **Tela de resultado** — pontuação final, nº de acertos, maior streak, tempo total.
5. **Salvar no ranking** — campo de nickname (opcional) para registrar a pontuação no leaderboard global.
6. **Leaderboard** — exibe as melhores pontuações.

### 2.2. Estrutura de uma partida
- **15 perguntas** por partida.
- **Dificuldade progressiva**: começa fácil e termina difícil.
  - Distribuição: **5 Iniciante → 5 Intermediário → 5 Avançado**.
  - As perguntas são selecionadas aleatoriamente dentro de cada faixa de dificuldade (sem repetir na mesma partida).
- As perguntas devem variar entre as 4 categorias temáticas (mix dentro de cada faixa).

### 2.3. Mecânicas de gameplay

#### Timer
- **15 segundos por pergunta**.
- Indicador visual de contagem regressiva (barra/círculo).
- Se o tempo esgotar: conta como **erro** e avança automaticamente, mostrando a resposta correta + explicação.

#### Sistema de pontuação
- **Base por acerto**: `100 pontos`.
- **Bônus de velocidade**: `+ (segundos restantes × 5)` pontos (máx. +75 se responder instantaneamente).
- **Bônus de streak** (acertos consecutivos): a partir do 3º acerto seguido, `+25` por acerto adicional na sequência.
- **Erro ou tempo esgotado**: `0 pontos` e zera o streak atual.
- Fórmula por pergunta acertada:
  ```
  pontos = 100 + (segundosRestantes * 5) + bonusStreak
  bonusStreak = streakAtual >= 3 ? (streakAtual - 2) * 25 : 0
  ```
- **Pontuação final** = soma dos pontos de todas as perguntas.
- Métricas exibidas no resultado: pontuação total, acertos/15, maior streak, tempo médio de resposta.

#### Níveis de dificuldade
- Cada pergunta tem um campo `difficulty`: `iniciante | intermediario | avancado`.
- Na V1 a dificuldade é **progressiva e automática** (não selecionável pelo usuário).
- *(Futuro)* Modo livre com escolha de dificuldade.

#### Ranking / Leaderboard
- Persistência **global** via **Supabase**.
- Registra: nickname, pontuação, nº de acertos, data.
- Exibe **Top 50** ordenado por pontuação (desc).
- Nickname é opcional: se vazio, salvar como "Anônimo" (ou não salvar, ver §2.4).

### 2.4. Features de experiência (UX)
- **Feedback educacional**: ao errar (ou em todas as respostas), mostrar:
  - Indicação de Verdadeiro/Falso correto.
  - **Explicação** textual (campo `explanation` da pergunta).
- **Nickname ao final**: campo opcional na tela de resultado para salvar no ranking.
- **Responsivo**: funciona bem em desktop e mobile.
- **Compartilhamento**: botão para copiar link / compartilhar resultado *(nice-to-have)*.

---

## 3. Conteúdo — Banco de Perguntas

### 3.1. Volume e persistência
- **30 a 50 perguntas** num arquivo **JSON local estático** (`data/questions.json`).
- Sem backend para as perguntas — fácil de editar e versionar via git.
- Distribuição balanceada entre dificuldades e categorias (mín. ~10 perguntas por dificuldade para garantir variedade nas partidas).

### 3.2. Categorias temáticas
1. **Fundamentos do Claude Code (CLI)** — o que é, instalação, comandos básicos, navegação.
2. **Features e Produtividade** — hooks, slash commands, MCP servers, subagents, plan mode.
3. **Claude API/SDK** — API da Anthropic, Agent SDK, tool use, prompt caching.
4. **Boas práticas e casos de uso** — CLAUDE.md, permissões, workflows, integração com IDEs.

### 3.3. Schema da pergunta (JSON)
```json
{
  "id": "q-001",
  "category": "fundamentos",          // fundamentos | features | api-sdk | boas-praticas
  "difficulty": "iniciante",          // iniciante | intermediario | avancado
  "statement": "O Claude Code pode ser executado diretamente no terminal via CLI.",
  "answer": true,                     // true = Verdadeiro, false = Falso
  "explanation": "Verdadeiro. O Claude Code é uma ferramenta de linha de comando (CLI) que roda no terminal, além de estar disponível em IDEs e na web."
}
```

### 3.4. Diretrizes de conteúdo
- Afirmações claras e inequívocas (sem ambiguidade entre V/F).
- Explicações curtas (1–3 frases), didáticas, com tom amigável.
- Conteúdo factualmente correto e atualizado sobre o Claude Code.
- Evitar pegadinhas injustas; o objetivo é educar, não enganar.

---

## 4. Especificação Técnica

### 4.1. Stack
| Camada | Tecnologia |
|---|---|
| Framework | **Next.js** (App Router) |
| Linguagem | **TypeScript** |
| Estilização | **Tailwind CSS** |
| Backend/Ranking | **Supabase** (PostgreSQL + API) |
| Hospedagem | **Vercel** (deploy automático via git) |
| Banco de perguntas | JSON estático local |

### 4.2. Estrutura de pastas (proposta)
```
01-quiz-claude-code/
├── app/
│   ├── page.tsx                 # Home
│   ├── quiz/page.tsx            # Tela de partida
│   ├── resultado/page.tsx       # Resultado + salvar ranking
│   ├── ranking/page.tsx         # Leaderboard
│   ├── layout.tsx
│   └── globals.css
├── components/
│   ├── QuestionCard.tsx
│   ├── Timer.tsx
│   ├── AnswerFeedback.tsx
│   ├── ScoreBoard.tsx
│   ├── ProgressBar.tsx
│   └── Leaderboard.tsx
├── lib/
│   ├── supabase.ts              # cliente Supabase
│   ├── scoring.ts               # lógica de pontuação
│   └── quiz.ts                  # seleção/ordenação de perguntas
├── data/
│   └── questions.json           # banco de perguntas
├── types/
│   └── index.ts                 # tipos TS (Question, GameState, ScoreEntry)
├── prd.md
└── README.md
```

### 4.3. Tipos principais (TypeScript)
```typescript
type Category = "fundamentos" | "features" | "api-sdk" | "boas-praticas";
type Difficulty = "iniciante" | "intermediario" | "avancado";

interface Question {
  id: string;
  category: Category;
  difficulty: Difficulty;
  statement: string;
  answer: boolean;
  explanation: string;
}

interface GameState {
  questions: Question[];
  currentIndex: number;
  score: number;
  correctCount: number;
  currentStreak: number;
  maxStreak: number;
  answers: { questionId: string; correct: boolean; timeSpent: number }[];
}

interface ScoreEntry {
  id?: string;
  nickname: string;
  score: number;
  correct_count: number;
  created_at?: string;
}
```

### 4.4. Schema do banco (Supabase)
Tabela `leaderboard`:
```sql
create table leaderboard (
  id uuid primary key default gen_random_uuid(),
  nickname text not null default 'Anônimo',
  score integer not null,
  correct_count integer not null,
  created_at timestamptz not null default now()
);

-- Índice para ordenação rápida do ranking
create index idx_leaderboard_score on leaderboard (score desc);

-- RLS: leitura pública, inserção pública (sem update/delete)
alter table leaderboard enable row level security;

create policy "leitura_publica" on leaderboard
  for select using (true);

create policy "insercao_publica" on leaderboard
  for insert with check (true);
```
> **Segurança**: usar a chave `anon` pública do Supabase no client. RLS restringe a apenas SELECT e INSERT (sem UPDATE/DELETE), evitando manipulação maliciosa do ranking. Validar `score` e tamanho do `nickname` no client antes de inserir.

### 4.5. Variáveis de ambiente
```
NEXT_PUBLIC_SUPABASE_URL=...
NEXT_PUBLIC_SUPABASE_ANON_KEY=...
```
> Documentar no README. Nunca commitar `.env.local`.

### 4.6. Lógica de seleção de perguntas
- Carregar `questions.json`.
- Filtrar por dificuldade e embaralhar dentro de cada faixa.
- Selecionar 5 iniciante + 5 intermediário + 5 avançado.
- Concatenar na ordem progressiva (iniciante → intermediário → avançado).
- Dentro de cada faixa, variar categorias quando possível.

---

## 5. Identidade Visual / Design

### 5.1. Tema
- **Dark mode** como padrão.
- Acento principal: **laranja Anthropic `#CC785C`**.
- Estilo **minimalista**, alinhado à estética oficial do Claude.

### 5.2. Paleta sugerida
| Uso | Cor |
|---|---|
| Fundo principal | `#1A1A1A` / `#0F0F0F` |
| Superfície / cards | `#262626` |
| Acento (botões, destaques) | `#CC785C` |
| Acerto | `#4ADE80` (verde) |
| Erro | `#F87171` (vermelho) |
| Texto primário | `#FAFAFA` |
| Texto secundário | `#A3A3A3` |

### 5.3. Diretrizes de UI
- Tipografia legível, espaçamento generoso.
- Animações sutis (transições de pergunta, contagem do timer).
- Feedback visual claro de acerto/erro (cor + ícone).
- Acessibilidade: contraste adequado, foco navegável por teclado, `aria-labels`.

---

## 6. Telas (Resumo)

| Tela | Rota | Conteúdo |
|---|---|---|
| Home | `/` | Título, descrição, "Iniciar Quiz", "Ver Ranking" |
| Quiz | `/quiz` | Card da pergunta, botões V/F, timer, barra de progresso, feedback |
| Resultado | `/resultado` | Pontuação, acertos, streak, campo nickname, "Salvar", "Jogar novamente" |
| Ranking | `/ranking` | Top 50 do leaderboard |

---

## 7. Deploy e Infraestrutura

- **Vercel**: deploy automático a cada push na branch principal.
- **Supabase**: projeto no free tier; tabela `leaderboard` com RLS.
- Configurar variáveis de ambiente no painel da Vercel.
- README com instruções de setup local e deploy.

---

## 8. Critérios de Aceite (Definition of Done)

- [ ] Usuário consegue jogar uma partida completa de 15 perguntas.
- [ ] Timer de 15s funciona; tempo esgotado conta como erro.
- [ ] Pontuação calculada com base + bônus de velocidade + streak.
- [ ] Dificuldade progressiva (5/5/5) com perguntas sem repetição na partida.
- [ ] Em cada resposta, exibe correto/incorreto + explicação.
- [ ] Tela de resultado mostra pontuação, acertos, maior streak.
- [ ] Usuário pode salvar pontuação com nickname no leaderboard (Supabase).
- [ ] Ranking global exibe Top 50 ordenado por pontuação.
- [ ] Tema dark com laranja Anthropic aplicado; responsivo.
- [ ] Banco com 30–50 perguntas válidas distribuídas por categoria/dificuldade.
- [ ] Deploy funcional na Vercel.

---

## 9. Roadmap Futuro (pós-V1)

- Modo livre com escolha de dificuldade/categoria.
- Outros formatos de pergunta (múltipla escolha).
- Compartilhamento de resultado em redes sociais (card de imagem).
- Internacionalização (EN).
- Painel admin para gerenciar perguntas.
- Autenticação para perfis persistentes.
- Modo "desafio diário".

---

## 10. Resumo das Decisões do Brainstorm

| Decisão | Escolha |
|---|---|
| Stack | Next.js + TypeScript + Tailwind |
| Formato | Verdadeiro ou Falso (único) |
| Mecânicas | Timer, pontuação, dificuldade, ranking |
| Banco de perguntas | 30–50 em JSON local |
| Persistência ranking | Supabase (global, free tier) |
| Categorias | Fundamentos CLI · Features/Produtividade · API/SDK · Boas práticas |
| Visual | Dark mode + laranja Anthropic (#CC785C) |
| Features extras | Explicação ao errar · nickname ao final |
| Estrutura da partida | 15 perguntas, dificuldade progressiva |
| Timer | 15 segundos por pergunta |
| Deploy | Vercel + Supabase |
| Idioma (V1) | Português |
