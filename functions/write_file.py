import os


def write_file(working_directory, file_path, content):
    try:
        abspath_wd = os.path.abspath(working_directory)
        full_path = os.path.join(working_directory, file_path)
        abspath_fp = os.path.abspath(full_path)
        if not abspath_fp.startswith(abspath_wd):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        with open(abspath_fp, "w") as f:
            f.write(content)

        result = (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )

    except Exception as e:
        result = f"Error: {str(e)}"

    return result
