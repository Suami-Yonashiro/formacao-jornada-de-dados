import Link from "next/link";

export default function Home() {
  return (
    <div
      className="min-h-screen flex flex-col items-center justify-center px-4 text-center"
      style={{ backgroundColor: "#0F0F0F" }}
    >
      <div className="max-w-lg w-full">
        <p
          className="text-xs font-semibold tracking-widest uppercase mb-4"
          style={{ color: "#CC785C" }}
        >
          Quiz
        </p>

        <h1 className="text-4xl sm:text-5xl font-bold mb-4 leading-tight" style={{ color: "#FAFAFA" }}>
          Domine o Claude Code
        </h1>

        <p className="text-base mb-10 leading-relaxed" style={{ color: "#A3A3A3" }}>
          15 perguntas de Verdadeiro ou Falso sobre o Claude Code.
          Teste seus conhecimentos em fundamentos, features, API e boas práticas.
          Dispute no ranking global.
        </p>

        <div className="flex flex-col sm:flex-row gap-3 justify-center">
          <Link
            href="/quiz"
            className="px-8 py-4 rounded-xl font-bold text-base transition-opacity hover:opacity-90"
            style={{ backgroundColor: "#CC785C", color: "#FAFAFA" }}
          >
            Iniciar Quiz
          </Link>
          <Link
            href="/ranking"
            className="px-8 py-4 rounded-xl font-bold text-base border transition-colors hover:bg-white/5"
            style={{ borderColor: "#333", color: "#A3A3A3" }}
          >
            Ver Ranking
          </Link>
        </div>

        <div className="mt-12 flex justify-center gap-6 text-xs" style={{ color: "#444" }}>
          <span>15 perguntas</span>
          <span>·</span>
          <span>3 dificuldades</span>
          <span>·</span>
          <span>Timer de 15s</span>
          <span>·</span>
          <span>Ranking global</span>
        </div>
      </div>
    </div>
  );
}
