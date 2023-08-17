"""
======================= NW DIAGNOSTIC UTILITY ==================================
https://github.com/denisecase/nw-diagnostics/
================================================================================

PURPOSE:
- Generate detailed information about the Python environment and system.
- Help detect common setup issues before they become bigger problems.
- Offer a standardized way to gather info across multiple projects.

ORIGIN:
This module is part of the NW Diagnostics hosted on GitHub. 
It's a centralized tool designed to aid instructors and students in 
  diagnosing and understanding their Python environment and system setup.

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
Copy this repo's 00_check_core.py file to your local repository.

================================================================================
To learn more or contribute, see the repository and its documentation.
================================================================================
"""

# Import from Python Standard Library

import datetime
import logging
import os
import platform
import shutil
import sys

# Setup logging

OUTPUT_FILENAME = "00_check_core.txt"
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    handlers=[logging.FileHandler(OUTPUT_FILENAME, mode="w"), logging.StreamHandler()],
)

# Declare additional program constants

DIVIDER = "=" * 70  # A string divider for cleaner output formatting

# Retrieve additional system information using platform and os modules

build_date, compiler = platform.python_build()
implementation = platform.python_implementation()
architecture = platform.architecture()[0]
user_home = os.path.expanduser("~")


# Define program functions


def check_core(fn):
    """
    Generates and prints debug information about the current system.

    Args:
    - fn (str): Path to the file for which the information should be generated.
    """
    debug_info = get_header(fn)
    logging.info(debug_info)


def get_terminal_info():
    """Determine the terminal and environment."""
    term_program = os.environ.get("TERM_PROGRAM", "")
    term_program_version = os.environ.get("TERM_PROGRAM_VERSION", "").lower()

    if term_program == "vscode":
        environment = "VS Code"
        if "powershell" in term_program_version:
            current_shell = "powershell"
        else:
            # Fallback approach for VS Code
            current_shell = (
                os.environ.get("SHELL", os.environ.get("ComSpec", ""))
                .split(os.sep)[-1]
                .lower()
            )
    else:
        environment = "Native Terminal"
        current_shell = (
            os.environ.get("SHELL", os.environ.get("ComSpec", ""))
            .split(os.sep)[-1]
            .lower()
        )

    return environment, current_shell


def get_source_directory_path():
    """
    Returns the absolute path to the directory containing this script.
    """
    dir = os.path.dirname(os.path.abspath(__file__))
    return dir


def is_git_in_path():
    """
    Checks if git is available in the PATH.

    Returns:
    - bool: True if git is in the PATH, otherwise False.
    """
    return shutil.which("git") is not None


def get_header(fn):
    """
    Constructs a formatted string that provides helpful information.

    Args:
    - fn (str): Path to the file for which the information should be generated.

    Returns:
    - str: Formatted debug information.
    """

    environment, current_shell = get_terminal_info()

    return f"""
{DIVIDER}
{DIVIDER}
 Welcome to NW Diagnostics!
 At: {datetime.date.today()} at {datetime.datetime.now().strftime("%I:%M %p")}
 Operating System: {os.name} {platform.system()} {platform.release()}
 System Architecture: {architecture}
 Number of CPUs: {os.cpu_count()}
 Machine Type: {platform.machine()}
 Python Version: {platform.python_version()}
 Python Build Date and Compiler: {build_date} with {compiler}
 Python Implementation: {implementation}
 Active pip environment: {os.environ.get('PIP_DEFAULT_ENV', 'None')}
 Path to Interpreter:         {sys.executable}
 Path to virtual environment: {sys.prefix}
 Current Working Directory:   {os.getcwd()}
 Path to source directory:    {get_source_directory_path()}
 Path to script file:         {fn}
 User's Home Directory:       {user_home}
 Terminal Environment:        {environment}
 Terminal Type:               {current_shell}
 Git available in PATH:       {is_git_in_path()} 
{DIVIDER}
{DIVIDER}
"""


def run_diagnostic_core(namespace=None):
    """Function to run the main diagnostic checks."""
    if namespace:
        check_core_func = namespace.get("check_core")
        if callable(check_core_func):
            check_core_func(__file__)
    else:
        check_core(__file__)

