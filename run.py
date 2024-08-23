import sys
import os
import subprocess

def run_script(script_name):
    """Run a given script using the virtual environment's Python interpreter."""
    if os.name == 'nt':  # For Windows
        venv_python = 'venv\\Scripts\\python.exe'
    else:  # For Unix-like systems
        venv_python = 'venv/bin/python'

    subprocess.check_call([venv_python, script_name] + sys.argv[1:])

if __name__ == "__main__":
    # Determine the path to the virtual environment's Python interpreter
    if 'venv' not in sys.executable:
        run_script('main.py')
    else:
        import main  # Import your main script here
