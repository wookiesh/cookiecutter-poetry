{% set is_open_source = cookiecutter.open_source_license != 'Not opensource' -%}

# {{ cookiecutter.project_name }}

{% if is_open_source %}
.. image:: <https://img.shields.io/pypi/v/>{{ cookiecutter.project_slug }}.svg
:target: <https://pypi.python.org/pypi/>{{ cookiecutter.project_slug }}

[![image](https://img.shields.io/travis/%7B%7B%20cookiecutter.github_username%20%7D%7D/%7B%7B%20cookiecutter.project_slug%20%7D%7D.svg)](https://travis-ci.org/%7B%7B%20cookiecutter.github_username%20%7D%7D/%7B%7B%20cookiecutter.project_slug%20%7D%7D)

[![Documentation Status](<https://readthedocs.org/projects/%7B%7B%20cookiecutter.project_slug%20%7C%20replace(%22_%22,%20%22-%22)%20%7D%7D/badge/?version=latest>)](<https://%7B%7B%20cookiecutter.project_slug%20%7C%20replace(%22_%22,%20%22-%22)%20%7D%7D.readthedocs.io/en/latest/?badge=latest>)

{%- endif %}

{{ cookiecutter.project_short_description }}

{% if is_open_source %}

- Free software: {{ cookiecutter.open_source_license }}
  {% if cookiecutter.create_docs == 'y' %}
- Documentation: <https://>{{ cookiecutter.project_slug |  replace("_", "-") }}.readthedocs.io.

{% endif %}
{% endif %}

# Features

- TODO

# Credits

This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[johanvergeer/cookiecutter-poetry](https://github.com/wookiesh/cookiecutter-poetry)
project template.
