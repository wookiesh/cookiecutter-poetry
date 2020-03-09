===================
Cookiecutter Poetry
===================

Cookiecutter_ template for a Python package.

* GitHub repo: https://github.com/johanvergeer/cookiecutter-poetry/
* Documentation: https://cookiecutter-poetry.readthedocs.io/
* Free software: MIT license

Features
--------

* Testing setup with ``unittest`` and ``python setup.py test`` or ``pytest``
* Travis-CI_: Ready for Travis Continuous Integration testing
* Tox_ testing: Setup to easily test for Python 3.6, 3.7, 3.8
* Sphinx_ docs: Documentation ready for generation with, for example, ReadTheDocs_
* Auto-release to PyPI_ when you push a new tag to master (optional)
* Command line interface using Click (optional)

.. _Cookiecutter: https://github.com/audreyr/cookiecutter

Build Status
-------------

Linux:

.. image:: https://img.shields.io/travis/johanvergeer/cookiecutter-poetry.svg
    :target: https://travis-ci.com/johanvergeer/cookiecutter-poetry
    :alt: Linux build status on Travis CI

Windows:

.. image:: https://ci.appveyor.com/api/projects/status/github/johanvergeer/cookiecutter-poetry?branch=master&svg=true
    :target: https://ci.appveyor.com/project/johanvergeer/cookiecutter-poetry/branch/master
    :alt: Windows build status on Appveyor

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet
(this requires Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/audreyr/cookiecutter-poetry.git

Then:

* Create a repo and put it there.
* Add the repo to your Travis-CI_ account.
* Install the dev requirements into a virtualenv. (``pip install -r requirements_dev.txt``)
* Register_ your project with PyPI.
* Run the Travis CLI command `travis encrypt --add deploy.password` to encrypt your PyPI password in Travis config
  and activate automated deployment on PyPI when you push a new tag to master branch.
* Add the repo to your ReadTheDocs_ account + turn on the ReadTheDocs service hook.
* Release your package by pushing a new tag to master.
* Add a `requirements.txt` file that specifies the packages you will need for
  your project and their versions. For more info see the `pip docs for requirements files`_.

.. _`pip docs for requirements files`: https://pip.pypa.io/en/stable/user_guide/#requirements-files
.. _Register: https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives

For more details, see the `cookiecutter-poetry tutorial`_.

.. _`cookiecutter-poetry tutorial`: https://cookiecutter-poetry.readthedocs.io/en/latest/tutorial.html

Fork This / Create Your Own
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. Or create your own; it doesn't strictly have to
be a fork.

* Once you have your own version working, add it to the Similar Cookiecutter
  Templates list above with a brief description.

* It's up to you whether or not to rename your fork/own version. Do whatever
  you think sounds good.

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~

I also accept pull requests on this, if they're small, atomic, and if they
make my own packaging experience better.


.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.io/
.. _bump2version: https://github.com/c4urself/bump2version
.. _Punch: https://github.com/lgiordani/punch
.. _Pipenv: https://pipenv.readthedocs.io/en/latest/
.. _PyPi: https://pypi.python.org/pypi