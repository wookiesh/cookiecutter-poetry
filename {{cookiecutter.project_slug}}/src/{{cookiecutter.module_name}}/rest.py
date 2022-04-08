"""main functions and logic."""

import logging

import rollbar

{% if cookiecutter.provide_rest_api == "y" -%}
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
{% endif %}

from . import __version__, configure_logging
{% if cookiecutter.provide_rest_api == "y" -%}from .api.v1.routes import router{% endif %}
from .config import Settings


logger = logging.getLogger(__name__)

{% if cookiecutter.provide_rest_api == "y" -%}
def create_app() -> FastAPI:
    """Application factory."""
    settings = Settings()
    if settings.environment != "dev":
        rollbar.init(
            settings.rollbar_token,
            settings.environment,
            code_version=__version__,
            handler="async",
            include_request_body=True,
        )

    def payload_hander(payload: dict) -> dict:
        """Add application name for rollbar tracking."""
        payload["data"]["application"] = __name__.split(".")[1]
        return payload

    rollbar.events.add_payload_handler(payload_hander)

    app = FastAPI(
        title="{{cookiecutter.project_short_description}}",
        version=f"{__version__} - {settings.environment}",
        contact={"name": "{{cookiecutter.full_name}}", "email":"{{cookiecutter.email}}"},
        # servers=[
        #     {"url": "https://adsb-qa.ana.lu", "description": "Staging environment"},
        #     {"url": "https://adsb.ana.lu", "description": "Production environment"},
        # ],
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.on_event("startup")
    def set_up() -> None:
        """When fastapi starts."""
        configure_logging(settings)
        logger.info("version: %s %s", __version__, settings.environment)

    @app.on_event("shutdown")
    def shutdown() -> None:
        """When fastapi stops."""

    # Set all CORS enabled origins
    if settings.cors_origins:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.cors_origins],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    app.include_router(router, prefix="/api/v1", tags=["API V1"])
    return app
{% endif %}
