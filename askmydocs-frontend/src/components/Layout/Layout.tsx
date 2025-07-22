import type { ReactNode } from "react";
import Sidebar from "../Sidebar/Sidebar";

interface LayoutProps {
  children: ReactNode;
}

export default function Layout({ children }: LayoutProps) {
  return (
    <div className="w-full min-h-screen bg-base-100 flex">
      <Sidebar files={[
        "relatorio-financeiro-jan.pdf",
        "relatorio-financeiro-fev.pdf",
        "relatorio-financeiro-mar.pdf",
        "relatorio-financeiro-abr.pdf",
        "relatorio-financeiro-mai.pdf"
      ]} />
      <main className="flex-1 p-4 flex flex-col items-center justify-center">
        {children}
      </main>
    </div>
  );
}
