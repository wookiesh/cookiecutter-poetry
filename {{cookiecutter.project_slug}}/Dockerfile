# Uses multi-stage builds requiring Docker 17.05 or higher

FROM python:3.10.2-slim-buster as builder

ENV PYTHONDONTWRITEBYTECODE=1  \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    POETRY_HOME="/root/.poetry"
# POETRY_VERSION=1.1.13 \


# build requirements
RUN apt-get update \
    && apt-get --no-install-recommends -y install curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

WORKDIR /app

COPY poetry.lock pyproject.toml ./
RUN --mount=type=cache,target=/root/.cache  ${POETRY_HOME}/bin/poetry install --no-dev

# final stage
FROM python:3.10.2-slim-buster
EXPOSE 8000/tcp

RUN groupadd -g 999 python && \
    useradd -r -u 999 -g python python
USER 999

WORKDIR /app
COPY --chown=python:python --from=builder /app/.venv ./.venv
COPY --chown=python:python ./src/${NAME} ./${NAME}
COPY --chown=python:python pyproject.toml {% if cookiecutter.provide_rest_api == "y" -%}misc/uvicorn-logging.yaml{% endif %} ./
RUN mkdir data

ENV PATH="/app/.venv/bin:$PATH"
ENTRYPOINT [ "uvicorn", "--host", "0.0.0.0" ]
