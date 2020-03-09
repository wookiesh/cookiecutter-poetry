Prompts
=======

When you create a package, you are prompted to enter these values.

Templated Values
----------------

The following appear in various parts of your generated project.

.. role:: bash(code)
   :language: bash

`full_name`
    Your full name.

`email`
    Your email address.

`github_username`
    Your GitHub username.

`project_name`
    The name of your new Python package project. This is used in documentation, so spaces and any characters are fine here.

`project_slug`
    Slugified name of your new Python project. Typically, it is the slugified version of project-name.
    
`module_name`
    The namespace of your Python package. This should be Python import-friendly. Typically, it is the slugified version with underscores of project_name.

`project_short_description`
    A 1-sentence description of what your Python package does.

`pypi_username`
    Your Python Package Index account username.

`version`
    The starting version number of the package.

`use_pypi_deployment_with_travis`
    Whether to deploy to Pypi with Travis CI

`command_line_interface`
    - none: Don't create a command line application.
    - click: Create a command line interface application using Click_.
    - argparse: Create a command line interface application using argparse_.

`create_author_file`
    Create `AUTHORS.rst` in the project root?

`create_docs`
    Create a `docs` directory?

`open_source_license`
    Select one of the open source licenses or "Not open source" when applicable.

`use_pycharm`
    Will PyCharm_ be used for this project?



Options
-------

The following package configuration options set up different features for your project.

use_pypi_deployment_with_travis
    Whether to use PyPI deployment with Travis.

command_line_interface
    Whether to create a console script using Click. Console script entry point will match the module_name. Options: ["Click", "None"]


.. _pyup.io: https://pyup.io
.. _Click: https://click.palletsprojects.com/en/7.x/
.. _argparse: https://docs.python.org/3/library/argparse.html
.. _PyCharm: https://www.jetbrains.com/pycharm/