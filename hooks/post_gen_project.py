#!/usr/bin/env python
import os
import shutil
from pathlib import Path

PROJECT_DIRECTORY = Path(".").absolute()


def remove(filepath):
    target = PROJECT_DIRECTORY / filepath

    if target.is_dir():
        shutil.rmtree(target, ignore_errors=True)
    else:
        target.unlink()


if __name__ == "__main__":

    if "{{ cookiecutter.create_author_file }}" != "y":
        remove("AUTHORS.md")
        # remove("docs/authors.md")

    # if "{{ cookiecutter.create_docs }}" != "y":
    #     remove("docs")

    if "none" in "{{ cookiecutter.command_line_interface|lower }}":
        cli_file = os.path.join("src", "{{ cookiecutter.module_name }}", "cli.py")
        print('no cli')
        print('{{cookiecutter.command_line_interface}}')
        remove(cli_file)

    if "Not open source" == "{{ cookiecutter.open_source_license }}":
        remove("LICENSE")

    if "n" == "{{ cookiecutter.use_vscode }}":
        remove('.vscode')

    if 'n' == "{{ cookiecutter.provide_rest_api }}":
        remove('src/{{cookiecutter.module_name}}/api')
        remove('src/{{cookiecutter.module_name}}/rest.py')

    remove("licenses")
