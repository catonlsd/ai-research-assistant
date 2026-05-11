import type { Metadata } from "next";
import { Nav } from "@/components/nav";
import "./globals.css";

export const metadata: Metadata = {
  title: "AI Research Assistant",
  description:
    "Production-style AI research assistant with multi-document RAG, web search, memory, and citations.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <div className="soft-grid min-h-screen bg-[#f8fbff] text-slate-900">
          <div className="flex min-h-screen">
            <Nav />
            <main className="min-w-0 flex-1 overflow-x-hidden p-4 sm:p-6 lg:p-8">
              {children}
            </main>
          </div>
        </div>
      </body>
    </html>
  );
}