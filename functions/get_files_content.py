import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    try:
        abspath_wd = os.path.abspath(working_directory)
        full_path = os.path.join(working_directory, file_path)
        abspath_fp = os.path.abspath(full_path)
        if not abspath_fp.startswith(abspath_wd):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(abspath_fp):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(abspath_fp, "r") as f:
            file_content_string = f.read(MAX_CHARS)

        if len(file_content_string) >= MAX_CHARS:
            file_content_string += f"[...File \"{file_path}\" truncated at 10000 characters]"

        result = file_content_string 
    except Exception as e:
        result = f"Error: {str(e)}"

    return result
