import { useState } from "react";
import { FiFileText, FiMenu, FiPlus } from "react-icons/fi";

interface SidebarProps {
  files: string[];
}

export default function Sidebar({ files }: SidebarProps) {
  const [isOpen, setIsOpen] = useState(false);

  const toggleSidebar = () => setIsOpen(!isOpen);

  return (
    <div className="flex flex-col h-screen bg-base-300 text-base-content">
      <button onClick={toggleSidebar} className="lg:hidden p-4">
        <FiMenu size={20} />
      </button>

      <aside
        className={`
                    ${isOpen ? "block" : "hidden"}
                    lg:block
                    flex flex-col w-60 px-4 py-6 space-y-6 text-sm    
                `}
      >
        <div className="text-lg font-semibold opacity-80 select-none">
          AskMyDocs
        </div>

        <button className="flex items-center gap-2 opacity-70 hover:opacity-100 transition-opacity">
          <FiPlus size={16} />
          <span>Importar arquivo</span>
        </button>

        <div className="flex-1 overflow-y-auto space-y-2">
          {files.length === 0 ? (
            <div className="opacity-50 text-sm">Nenhum arquivo carregado.</div>
          ) : (
            files.map((file, index) => (
              <button
                key={index}
                className="flex items-center gap-2 w-full text-left opacity-70 hover:opacity-100 transition-opacity truncate"
              >
                <FiFileText size={14} />
                <span className="text-sm truncate">{file}</span>
              </button>
            ))
          )}
        </div>
      </aside>
    </div>
  );
}
