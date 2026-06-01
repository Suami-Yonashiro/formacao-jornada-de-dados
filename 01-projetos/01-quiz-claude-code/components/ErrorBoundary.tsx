"use client";

import { Component, type ReactNode, type ErrorInfo } from "react";
import Link from "next/link";

interface Props {
  children: ReactNode;
}

interface State {
  hasError: boolean;
  error: Error | null;
}

export default class ErrorBoundary extends Component<Props, State> {
  state: State = { hasError: false, error: null };

  static getDerivedStateFromError(error: Error): State {
    return { hasError: true, error };
  }

  componentDidCatch(error: Error, info: ErrorInfo) {
    console.error("[ErrorBoundary]", error, info);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div
          className="min-h-screen flex flex-col items-center justify-center px-4 text-center"
          style={{ backgroundColor: "#0F0F0F" }}
        >
          <p
            className="text-xs font-semibold tracking-widest uppercase mb-4"
            style={{ color: "#F87171" }}
          >
            Erro inesperado
          </p>
          <h1 className="text-2xl font-bold mb-2" style={{ color: "#FAFAFA" }}>
            Algo deu errado
          </h1>
          <p className="text-sm mb-8" style={{ color: "#A3A3A3" }}>
            {this.state.error?.message ?? "Tente novamente."}
          </p>
          <div className="flex gap-3">
            <button
              onClick={() => this.setState({ hasError: false, error: null })}
              className="px-6 py-3 rounded-xl font-bold text-sm transition-opacity hover:opacity-90"
              style={{ backgroundColor: "#CC785C", color: "#FAFAFA" }}
            >
              Tentar novamente
            </button>
            <Link
              href="/"
              className="px-6 py-3 rounded-xl font-bold text-sm border transition-colors hover:bg-white/5"
              style={{ borderColor: "#404040", color: "#A3A3A3" }}
            >
              Início
            </Link>
          </div>
        </div>
      );
    }

    return this.props.children;
  }
}
