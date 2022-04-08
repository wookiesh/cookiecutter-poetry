"""Application settings and parameters."""

from typing import Literal
from pydantic import  BaseSettings


class Settings(BaseSettings):
    """Main settings (env based)."""

    {% if cookiecutter.provide_rest_api == "y" -%}cors_origins: list = ['*']{% endif %}
    environment: Literal["dev", "qa", "prod"] = "dev"
    log_level: Literal["DEBUG", "INFO", "WARNIING", "ERROR"] = "DEBUG"
    rollbar_token: str | None

    class Config:
        """Config class."""

        env_file = ".env"
        {% if cookiecutter.use_docker_swarm == "y" -%}secrets_dir = "/run/secrets"{% endif %}
