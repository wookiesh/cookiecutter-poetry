"""Console script for {{cookiecutter.module_name}}."""

import typer

from . import configure_logging
from .config import Settings

app = typer.Typer()


@app.command()
def main(
    debug: bool = typer.Option(False, "-d", "--debug", help="display logging information"),
) -> None:
    """Run this cli to do something magical."""
    settings = Settings()
    configure_logging(settings)

    if debug:
        typer.secho("lets debug!", fg=typer.colors.RED)


if __name__ == "__main__":
    app()
