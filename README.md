# nw-diagnostics-python

> Utility files to help debug installations and environments for Python projects.

## Overview

The `nw-diagnostics-python` repository provides a set of diagnostic scripts and utilities designed to aid instructors, students, and developers in diagnosing and understanding their Python system setup.

These scripts offer help with opinionated installations.

- We recommend [Visual Studio Code](https://code.visualstudio.com/) and [Git](https://git-scm.com/).
- We use [Python 3.8 or greater](https://www.python.org/downloads/) and built-in pip for package management.
- We use built-in [venv](https://docs.python.org/3/library/venv.html) to create and activate virtual environments.
- We create a `.venv` local folder in the root of a project repository to store the virtual environment.
- We use a requirements.txt file to manage third-party dependencies.

Other options can be implemented using these examples. 

## Getting Started

The scripts in the root folder are designed to be run locally on a developer's machine and to help set up and verify the local development environment.

To use them:

1. Identify and copy the desired local example file (e.g., `00_check_core.py` for basic checks or `00_check_env.py` for environment checks) to the root folder of your local repository.
1. Run the script on your machine, in your project repository. 
1. Review the console output and/or text file generated. 

## Directory Structure For the Remote Code

Most users do not need to directly access the remote code. It is written once and shared across multiple courses and projects.

- `basic`: Scripts to check basic machine configuration and Python installation.
- `environment`: Scripts to check local virtual environment and third-party dependencies.
- `external`: Scripts to check third-party dependencies, installations, and configurations.

## Caution

These utilities execute code fetched from remote sources. 
Always ensure the sources are trusted and be aware of potential risks associated with executing such scripts.

## Contributing

We welcome contributions to improve these utilities or add new ones. 
If you'd like to contribute, please fork the repository and use a feature branch. 
Pull requests are welcomed.

## Links

- Repository: [https://github.com/denisecase/nw-diagnostics-python](https://github.com/denisecase/nw-diagnostics-python)
- Issue tracker: [https://github.com/denisecase/nw-diagnostics-python/issues](https://github.com/denisecase/nw-diagnostics-python/issues)
