"""
======================= NW DIAGNOSTIC UTILITY ==================================
https://github.com/denisecase/nw-diagnostics/
================================================================================

PURPOSE:
- Generate detailed information about the Python virtual environment.
- Help detect common setup issues before they become bigger problems.
- Offer a standardized way to gather info across multiple projects.

ORIGIN:
This module is part of the NW Diagnostics hosted on GitHub. 
It's a centralized tool designed to aid instructors and students in 
  diagnosing and understanding their Python virtual environments.

NOTES:
This is a utility module. It's designed to be imported and its functions 
  used in other scripts, rather than being executed directly.
This module exclusively uses modules from the Python standard library, ensuring 
  compatibility without additional installations.

USAGE:
Execute the function, which will display information 
   in the terminal and save it to a designated file.
If you encounter setup issues, refer to the outputs of this module 
   for insights. The information can be shared to facilitate debugging.

LOCALLY:
Copy this repo's 00_check_env.py file to your local repository.

================================================================================
To learn more or contribute, see the repository and its documentation.
================================================================================
"""

# Python Standard Library

import datetime
import logging
import os
import sys

# Setup logging

OUTPUT_FILENAME = "00_check_env.txt"
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[logging.FileHandler(OUTPUT_FILENAME, mode="w"), logging.StreamHandler()],
)

# Declare additional program constants

DIVIDER = "=" * 70  # A string divider for cleaner output formatting
CREATE_COMMAND = "python -m venv .venv"
ACTIVATE_COMMAND_WINDOWS = ".venv\\Scripts\\activate"
ACTIVATE_COMMAND_MAC_LINUX = "source .venv/bin/activate"
UPGRADE_COMMAND = "python -m pip install --upgrade pip"
INSTALL_COMMAND = "python -m pip install"
INSTALL_COMMAND_WITH_REQUIREMENTS_FILE = "python -m pip install -r requirements.txt"

SUCCESS_MESSAGE = """
All checks passed successfully! Your environment is set up correctly.
If it asks you to upgrade pip, please do so using the suggested command.
"""

NO_REQUIREMENTS_FILE_MESSAGE = """
WARNING: No requirements.txt file found.
SOLUTION: Create a new requirements.txt file in the repo folder. 
          In the file, list each external dependency on a separate line.
"""

MISSING_DEPENDENCY_MESSAGE = f"""
SOLUTION: Add the missing dependency to requirements.txt and install by running: 
{INSTALL_COMMAND_WITH_REQUIREMENTS_FILE}
"""


# Define program functions


def get_activate_command():
    """Returns the command to activate the virtual environment."""
    if sys.platform == "win32":
        return ACTIVATE_COMMAND_WINDOWS
    else:
        return ACTIVATE_COMMAND_MAC_LINUX


def check_for_dotvenv_folder():
    """Checks if the .venv folder exists."""
    if os.path.exists(".venv"):
        return {"status": "success", "message": "YAY! .venv directory exists."}
    else:
        return {
            "status": "error",
            "message": f"ERROR: Missing .venv directory. Create it (may take a while) using: {CREATE_COMMAND}",
        }


def check_dotvenv_is_active():
    """Checks if the .venv virtual environment is active."""
    venv_path = os.environ.get("VIRTUAL_ENV")
    if venv_path and ".venv" in venv_path:
        return {
            "status": "success",
            "message": "YAY! The .venv virtual environment is active.",
        }
    else:
        return {
            "status": "error",
            "message": f"ERROR: Activate the .venv virtual environment using: {get_activate_command()}",
        }


def check_requirements_file_exists():
    """Check if requirements.txt exists."""
    if os.path.exists("requirements.txt"):
        return {"status": "success", "message": "YAY! requirements.txt file exists."}
    else:
        return {"status": "error", "message": NO_REQUIREMENTS_FILE_MESSAGE}


def get_search_path_string():
    paths = "\n".join(sys.path)
    return f"""
Python's package search paths:
{"-" * 40}
{paths}
{"-" * 40}
"""


def log_with_divider(message):
    """Logs a message and the DIVIDER."""
    logging.info(message)
    logging.info(DIVIDER)


def read_dependencies():
    """Read dependencies from requirements.txt and return a list of package names."""
    if not check_requirements_file_exists():
        return []

    with open("requirements.txt", "r") as f:
        # Use list comprehension to extract package names
        return [line.split("==")[0].strip() for line in f.readlines()]


def is_dependency_installed(dependency):
    """Check if a given dependency is installed."""
    try:
        __import__(dependency)
        return True
    except ImportError:
        return False


def check_dependencies_installed_in_dotvenv():
    """Checks if dependencies are installed in the virtual environment."""
    dependencies = read_dependencies()

    # Use list comprehensions for results
    return [
        {
            "status": "success" if is_dependency_installed(dep) else "error",
            "message": (
                f"YAY! {dep} is installed in the .venv.\n{DIVIDER}"
                if is_dependency_installed(dep)
                else f"ERROR: {dep} is not installed in .venv. {MISSING_DEPENDENCY_MESSAGE}"
            ),
        }
        for dep in dependencies
    ]


def check_env(fn):
    """
    Generates and prints debug information about the current Python environment.

    Args:
    - fn (str): Path to the file for which the information should be generated.
    """
    logging.info(DIVIDER)
    logging.info("Welcome to NW Diagnostics!")
    logging.info(
        f"At: {datetime.date.today()} at {datetime.datetime.now().strftime('%I:%M %p')}"
    )

    results = []
    checks = [
        check_for_dotvenv_folder,
        check_dotvenv_is_active,
        check_requirements_file_exists,
        check_dependencies_installed_in_dotvenv,
    ]

    for check in checks:
        result = check()
        if isinstance(result, list):
            for individual_result in result:
                logging.info(individual_result["message"])
            results.extend(result)
            # Check if any individual check resulted in an error
            if any(item["status"] == "error" for item in result):
                break
        else:
            logging.info(result["message"])  # Log the message of each result
            results.append(result)
            logging.info(DIVIDER)  # Separate each result with a divider

        # if result exists and the type is dict and the status is error, break
        if result and isinstance(result, dict):
            if result["status"] == "error":
                break

    return results


def run_diagnostic_env(namespace=None):
    """Function to run the main diagnostic checks."""
    if namespace:
        check_env_func = namespace.get("check_env")
        if callable(check_env_func):
            check_env_func(__file__)
    else:
        check_env(__file__)
