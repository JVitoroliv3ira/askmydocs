import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock
from expression.core import Result, Success

from askmydocs_backend.ingestion.pdf_loader import extract_text, load_pdf
from askmydocs_backend.domain.document import RawDocument

@patch("askmydocs_backend.ingestion.pdf_loader.pdfplumber.open")
def test_load_pdf_success(mock_open):
    mock_pdf = MagicMock()
    mock_pdf.pages = [MagicMock(), MagicMock()]
    mock_pdf.pages[0].extract_text.return_value = "Page 1"
    mock_pdf.pages[1].extract_text.return_value = "Page 2"
    mock_open.return_value.__enter__.return_value = mock_pdf

    mock_path = MagicMock(spec=Path)
    mock_path.name = "fake.pdf"
    mock_path.stat.return_value.st_size = 123

    result = load_pdf(mock_path)

    assert result.is_ok()
    doc = result.ok
    assert isinstance(doc, RawDocument)
    assert "Page 1" in doc.content
    assert "Page 2" in doc.content
    assert doc.metadata["pages"] == 2
    assert doc.metadata["size_bytes"] == 123

@patch("askmydocs_backend.ingestion.pdf_loader.pdfplumber.open")
def test_load_pdf_empty(mock_open):
    mock_pdf = MagicMock()
    mock_pdf.pages = [MagicMock()]
    mock_pdf.pages[0].extract_text.return_value = None
    mock_open.return_value.__enter__.return_value = mock_pdf
    
    mock_path = MagicMock(spec=Path)
    mock_path.name = "fake.pdf"
    
    result = load_pdf(mock_path)
    
    assert result.is_error()
    assert isinstance(result.error, ValueError)
    assert "vazio" in str(result.error).lower()

@patch("askmydocs_backend.ingestion.pdf_loader.pdfplumber.open")
def test_load_pdf_exception(mock_open):
    mock_open.side_effect = OSError("Falha ao abrir o arquivo")

    mock_path = MagicMock(spec=Path)
    mock_path.name = "corrupto.pdf"

    result = load_pdf(mock_path)

    assert result.is_error()
    assert isinstance(result.error, OSError)
    assert "falha" in str(result.error).lower()

@patch("askmydocs_backend.ingestion.pdf_loader.pdfplumber.open")
def test_load_pdf_whitespace_only(mock_open):
    page = MagicMock()
    page.extract_text.return_value = "   \n  \t  "
    
    mock_pdf = MagicMock()
    mock_pdf.pages = [page]
    mock_open.return_value.__enter__.return_value = mock_pdf

    mock_path = MagicMock(spec=Path)
    mock_path.name = "branco.pdf"

    result = load_pdf(mock_path)

    assert result.is_error()
    assert isinstance(result.error, ValueError)

def test_extract_text_path_does_not_exist():
    fake_path = Path("/caminho/inexistente/abc.pdf")
    result = extract_text(fake_path)

    assert result.is_error()
    assert isinstance(result.error, FileNotFoundError)

def test_extract_text_no_pdfs(tmp_path):
    result = extract_text(tmp_path)

    assert result.is_error()
    assert isinstance(result.error, ValueError)
    assert "nenhum pdf" in str(result.error).lower()

@patch("askmydocs_backend.ingestion.pdf_loader.load_pdf")
def test_extract_text_single_valid_file(mock_load_pdf, tmp_path):
    fake_pdf = tmp_path / "doc.pdf"
    fake_pdf.write_text("dummy content")

    mock_load_pdf.return_value = Success(RawDocument(
        content="texto",
        path=fake_pdf,
        metadata={"pages": 1, "size_bytes": 123}
    ))

    result = extract_text(fake_pdf)
    assert result.is_ok()
    assert len(result.ok) == 1
    assert result.ok[0].content == "texto"

@patch("askmydocs_backend.ingestion.pdf_loader.load_pdf")
def test_extract_text_all_fail(mock_load_pdf, tmp_path):
    (tmp_path / "fail1.pdf").write_text("...")
    (tmp_path / "fail2.pdf").write_text("...")

    mock_load_pdf.return_value = Result.Error(ValueError("quebrou"))

    result = extract_text(tmp_path)

    assert isinstance(result, Result)
    assert result.is_error()
