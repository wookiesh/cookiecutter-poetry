"""Deployment and misc tasks for the project."""

from os import system
from pathlib import Path
from tempfile import NamedTemporaryFile

import toml
from dotenv import dotenv_values
from fabric import task
from invoke import run
from jinja2 import Environment, FileSystemLoader

env = dotenv_values(".env")
jja = Environment(loader=FileSystemLoader("."), autoescape=True)

HOSTS = ("{{cookiecutter.deploy_host}}",)
ENVIRONMENT = "qa"
NAME = toml.load("pyproject.toml").get("tool").get("poetry").get("name").replace("-", "_")
# PATH = f"/srv/docker/prod/{NAME}"
VERSION = run("poetry version -s", hide=True).stdout.strip()


def create_sticky_folder(con, path, user="`whoami`", group="docker"):
    """For all in the group to have access but still knowing who did what."""
    con.sudo(f"mkdir -p {path}")
    con.sudo(f"chmod g+sw {path}")
    con.sudo(f"chown -R {user}:{group} {path}")


def get_path(environment: str, name: str = NAME, gluster_fs=True) -> Path:
    """Generate correct project path."""
    return Path(f"/{'mnt/gfs' if gluster_fs else 'srv'}/docker/{environment}/{name}")


def put_render(con, src: str, dest: Path, **kwargs):
    """Fabric put with rendered string."""
    content = jja.get_template(src).render(**kwargs)
    with NamedTemporaryFile() as temp:
        temp.write(content.encode("UTF-8"))
        temp.flush()
        con.put(temp.name, dest.as_posix())


@task
def lint(_):
    """Run all defined linters (pre-commit biased) on code and files."""
    system(
        """
        black .
        flake8
        pylint --enable-all-extensions src tests fabfile.py
        prospector
        toml-sort -ia pyproject.toml
    """
    )


@task
def check(_):
    """Run longer or 'harder' tests on the code base."""
    system(
        """
        safety check
        pytest --cov
        mypy --install-types --ignore-missing-imports src
        pip list --format=freeze | skjold -v audit --sources gemnasium -
        semgrep --config auto --quiet --exclude poetry.lock --exclude fabfile.py
    """
    )


@task
def build(_, version=VERSION, environment=ENVIRONMENT):
    """Build docker image and publish it, not be needed anymore with CI."""
    if version != VERSION:
        version = run(f"poetry version {version}").stdout.split()[-1].strip()

    system(
        f"""
        docker login hub.ana.lu
        export DOCKER_BUILDKIT=1
        docker buildx build --platform linux/amd64 -t hub.ana.lu/{NAME}-{environment}:{version} .
        """
    )
    return version


@task
def publish(_, version=VERSION, environment=ENVIRONMENT):
    """Publish the last created image to hub.ana.lu."""
    system(f"docker push hub.ana.lu/{NAME}-{environment}:{version}")


@task(hosts=HOSTS)
def setup(con, environment=ENVIRONMENT):
    """Create required folder structure and ..."""
    create_sticky_folder(con, get_path(environment))
    if (env_file := Path(f".env.{environment}")).exists():
        env.update(**dotenv_values(env_file))


@task(hosts=HOSTS)
def deploy(con, version=VERSION, environment=ENVIRONMENT):
    """Push and update docker-compose file on target and update containeur."""
    env.update(**dotenv_values(f".env.{environment}"))
    path = get_path(environment)
    put_render(
        con,
        "misc/templates/stack.yaml.jinja",
        path / "stack.yaml",
        name=NAME,
        environment=environment,
        version=version,
        ping_url=env.get("ping_url"),
    )
    with con.cd(path):
        con.run(f"docker stack deploy --with-registry-auth -c stack.yaml {NAME}")


@task(hosts=HOSTS)
def make(c, version=VERSION, environment=ENVIRONMENT):
    """Build, publish, and deploy."""
    version = build(c, version, environment)
    publish(c, version, environment)
    deploy(c, version, environment)
