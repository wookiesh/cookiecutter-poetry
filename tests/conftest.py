from pathlib import Path

import pytest


@pytest.fixture
def project_root_dir() -> Path:
    """The cookiecutter-poetry project path"""
    return Path().absolute().parent


@pytest.fixture
def docs_dir(project_root_dir) -> Path:
    return project_root_dir / "docs"
