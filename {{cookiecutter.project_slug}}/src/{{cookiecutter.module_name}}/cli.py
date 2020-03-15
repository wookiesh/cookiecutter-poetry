"""Console script for {{cookiecutter.module_name}}."""
import sys

{%- if cookiecutter.command_line_interface|lower == 'click' %}
import click

{%- endif %}

{% if cookiecutter.command_line_interface|lower == 'click' %}
@click.command()
def main(args=None):
    """Console script for {{cookiecutter.module_name}}."""
    click.echo(
        "Replace this message by putting your code into "
        "{{cookiecutter.module_name}}.cli.main"
    )
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


{%- endif %}


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
