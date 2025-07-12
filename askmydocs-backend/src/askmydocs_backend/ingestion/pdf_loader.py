from pathlib import Path
from typing import List
from expression.core import Result, Success, Failure
import pdfplumber

from askmydocs_backend.domain.document import RawDocument
from askmydocs_backend.core.functional import traverse_results

# TODO: permitir processamento parcial dos arquivos
def extract_text(path: Path) -> Result[List[RawDocument], Exception]:
    try:
        if not path.exists():
            return Failure(FileNotFoundError(f"Caminho não encontrado: {path.absolute()}"))
        
        files = [path] if path.is_file() else list(path.rglob("*.pdf"))
        if not files:
            return Failure(ValueError(f"Nenhum PDF encontrado em: {path}"))
        
        results = [load_pdf(p) for p in files]
        
        return traverse_results(results).filter(
            lambda docs: len(docs) > 0,
            default=ValueError("Nenhum conteúdo legível encontrado nos PDFs.")
        )
        
    except Exception as e:
        return Failure(e)

def load_pdf(path: Path) -> Result[RawDocument, Exception]:
    try:
        with pdfplumber.open(path) as pdf:
            text = "\n\n".join(page.extract_text() or "" for page in pdf.pages)
            
            if not text.strip():
                return Failure(ValueError(f"Arquivo vazio: {path.name}"))
            
            return Success(RawDocument(
                content=text,
                path=path,
                metadata={
                    "pages": len(pdf.pages),
                    "size_bytes": path.stat().st_size
                }
            ))
    except Exception as e:
        return Failure(e)
