"""
======================= NW DIAGNOSTIC UTILITY ==================================
https://github.com/denisecase/nw-diagnostics/
================================================================================

ORIGIN:
This is an instructor-generated script. You do not need to edit or understand 
  the code in this file. 

PURPOSE:
Generate detailed information about the local machine and its Python installation.

USAGE:
In the terminal, run the following command:  

python 00_check_core.py

OUTPUT:
See the new file named `00_check_core.txt` in your local repository.

REQUIREMENTS:
An active internet connection is required to fetch the diagnostic utility from 
  the GitHub repository.

CAUTION:
This script fetches and executes Python code from a remote source using 
  the `exec` function. While efforts have been made to ensure the security and 
  integrity of the hosted code, always be cautious and aware of the potential 
  risks associated with executing remote code. Ensure that the URL 
  (https://github.com/denisecase/nw-diagnostics/) is trusted before running the script.


================================================================================

"""


import urllib.request

URL = "https://raw.githubusercontent.com/denisecase/nw-diagnostics/main/nw_check_core.py"

def fetch_remote_code_and_execute(url):
    """
    Fetch Python code from a remote URL and execute it.
    
    Args:
    - url (str): The URL to fetch the Python code from.
    
    Returns:
    - dict: Dictionary containing the local scope after execution. 
    """
    local_scope = {}
    try:
        with urllib.request.urlopen(url) as response:
            code = response.read().decode('utf-8')
            exec(code, {}, local_scope)
    except Exception as e:
        print(f"Failed to fetch and execute code from {url}. Reason: {e}")
    
    return local_scope

# Fetch and execute the remote code
local_scope = fetch_remote_code_and_execute(URL)

# ---------------------------------------------------------------------------
# If this is the script we are running, then call some functions and execute code!
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    run_diagnostic = local_scope.get('run_diagnostic')
    if run_diagnostic:
        run_diagnostic()
    else:
        print("Failed to fetch or find the run_diagnostic function.")
