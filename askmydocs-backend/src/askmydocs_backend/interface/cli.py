import typer
from pathlib import Path
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
        typer.secho(f"Ocorreu um erro ao indexar os documentos: {result.error}")
    

@app.command("hello")
def hello_command() -> None:
    typer.echo("Hello, World!")

if __name__ == '__main__':
    app()
