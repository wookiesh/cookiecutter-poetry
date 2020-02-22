import re
import sys

MODULE_REGEX = re.compile(r"^[_a-zA-Z][_a-zA-Z0-9]+$")

module_name = "{{ cookiecutter.project_slug }}"

if not MODULE_REGEX.match(module_name):
    print(
        f"ERROR: The project slug ({module_name}) is not a valid Python module name. Please do not use a - and use _ instead"
    )

    # Exit to cancel project
    sys.exit(1)
