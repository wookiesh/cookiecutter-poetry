"""Top-level package for {{ cookiecutter.project_name }}.

Set version and handle log configuration.
"""

import logging
from importlib import metadata

import toml

from .config import Settings

try:
    from rich.logging import RichHandler
except ModuleNotFoundError:
    RICH = False
else:
    RICH = True

try:
    __version__ = metadata.version(__package__)
except metadata.PackageNotFoundError:
    __version__ = toml.load("pyproject.toml")["tool"]["poetry"]["version"]


def configure_logging(settings: Settings) -> None:
    """Configure logging, to be used at app startup."""
    handler = RichHandler(rich_tracebacks=True) if RICH else logging.StreamHandler()
    fmt = "%(message)s" if RICH else "%(asctime)s | %(levelname)-9s | %(name)s - %(message)s"

    logging.basicConfig(level=settings.log_level, format=fmt, handlers=[handler], force=True)
    logging.getLogger("multipart.multipart").setLevel(
        max(logging.INFO, getattr(logging, settings.log_level))
    )
