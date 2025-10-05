import os
from subprocess import run


def run_python_file(working_directory, file_path, args=[]):
    try:
        abspath_wd = os.path.abspath(working_directory)
        full_path = os.path.join(working_directory, file_path)
        abspath_fp = os.path.abspath(full_path)

        if not abspath_fp.startswith(abspath_wd):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.exists(abspath_fp):
            return f'Error: File "{file_path}" not found.'

        if not abspath_fp.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        cp = run(
            ["uv", "run", abspath_fp, *args],
            timeout=30,
            capture_output=True,
            text=True,  
            cwd=abspath_wd  
        )

        stdout = cp.stdout if cp.stdout else "No output produced."
        stderr = cp.stderr if cp.stderr else ""

        result = f"STDOUT:\n{stdout}\n\nSTDERR:\n{stderr}\n"

        if cp.returncode != 0:
            result += f"\nProcess exited with code {cp.returncode}"

    except Exception as e:
        result = f"Error: executing Python file: {e}"

    return result
