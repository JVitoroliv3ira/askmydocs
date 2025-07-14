import typer
from pathlib import Path
from askmydocs_backend.pipeline.ask_documents import ask_documents_pipeline
from askmydocs_backend.pipeline.index_documents import index_documents_pipeline

app = typer.Typer(help="ask-my-docs CLI")

@app.command("index")
def index_command(
    path: Path = typer.Argument(..., help="Caminho para o arquivo ou diretório com PDFs"),
    collection: str = typer.Option("public", help="Nome da coleção no Qdrant")
) -> None:
    result = index_documents_pipeline(
        path,
        collection
    )
    
    
    if result.is_ok():
        typer.echo("Documentos indexados com sucesso!")
    else:
        typer.secho(f"Ocorreu um erro ao indexar os documentos: {result.error}", err=True)
    

@app.command("ask")
def ask_command(
    question: str = typer.Argument(..., help="Pergunta a ser feita"),
    document_name: str = typer.Argument(..., help="Nome do documento para filtrar a busca"),
    collection: str = typer.Option("public", help="Nome da coleção no Qdrant"),
    top_k: int = typer.Option(5, help="Quantidade de chunks similares a buscar")
) -> None:
    result = ask_documents_pipeline(
        question,
        document_name,
        collection,
        top_k
    )

    if result.is_ok():
        typer.echo(result.ok)
    else:
        typer.secho(f"Ocorreu um erro ao buscar a resposta: {result.error}", err=True)

if __name__ == '__main__':
    app()
