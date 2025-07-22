import { useRef, useState } from "react";
import UploadImage from "../../assets/upload.svg";

interface UploadAreaProps {
  onFilesSelected: (files: File[]) => void;
}

export default function UploadArea({ onFilesSelected }: UploadAreaProps) {
  const [isDragging, setIsDragging] = useState(false);
  const inputRef = useRef<HTMLInputElement>(null);

  const handleFiles = (files: FileList | null) => {
    if (!files) return;
    onFilesSelected(Array.from(files));
  };

  return (
    <div className="w-full p-8">
      <div
        className={`
          w-full h-64 flex flex-col items-center justify-center 
          border-2 border-dashed rounded-md transition-all
          ${
            isDragging
              ? "bg-base-300 ring-1 ring-base-300"
              : "bg-base-100 border-base-content/10"
          }
          cursor-pointer
        `}
        onDragOver={(e) => {
          e.preventDefault();
          setIsDragging(true);
        }}
        onDragLeave={() => setIsDragging(false)}
        onDrop={(e) => {
          e.preventDefault();
          setIsDragging(false);
          handleFiles(e.dataTransfer.files);
        }}
        onClick={() => inputRef.current?.click()}
      >
        <input
          ref={inputRef}
          type="file"
          multiple
          onChange={(e) => handleFiles(e.target.files)}
          className="hidden"
        />

        <div className="flex flex-col items-center text-center space-y-4">
          <img src={UploadImage} alt="Upload" className="w-32 opacity-80" />
          <p className="text-sm opacity-70">
            {isDragging
              ? "Solte os arquivos aqui"
              : "Arraste ou clique para importar arquivos"}
          </p>
        </div>
      </div>
    </div>
  );
}
