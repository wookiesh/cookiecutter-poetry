"""Console script for {{cookiecutter.module_name}}."""

import typer

from . import configure_logging
from .config import Settings

app = typer.Typer()


@app.command()
def main() -> None:
    """Main application entry point."""
    settings = Settings()
    configure_logging(settings)


if __name__ == "__main__":
    app()
