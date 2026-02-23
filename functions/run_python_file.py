import os
from subprocess import run


def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_file = (
            os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        )
        if not valid_target_file:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        command = ["uv", "run", target_file]
        if args is not None:
            command.extend(*args)

        cp = run(
            command,
            timeout=30,
            capture_output=True,
            text=True,
            cwd=working_dir_abs,
        )

        stdout = cp.stdout if cp.stdout is not None else "No output produced."
        stderr = cp.stderr if cp.stderr is not None else "No output produced."

        result = f"STDOUT:\n{stdout}\nSTDERR:\n{stderr}\n"

        if cp.returncode != 0:
            result += f"\nProcess exited with code {cp.returncode}"

    except Exception as e:
        result = f"Error: executing Python file: {e}"

    return result
