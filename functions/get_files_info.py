import os


def get_files_info(working_directory, directory="."):
    try:
        abspath_wd = os.path.abspath(working_directory)
        full_path = os.path.join(working_directory, directory)
        abspath_fp = os.path.abspath(full_path)
        if not abspath_fp.startswith(abspath_wd):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(abspath_fp):
            return f'Error: "{directory}" is not a directory'

        files = os.listdir(abspath_fp)
        result = ""
        for file in files:
            path = os.path.join(abspath_fp, file)
            is_dir = os.path.isdir(path)
            file_size = os.path.getsize(path)
            result += f" - {file}: file_size:{file_size} bytes, is_dir={is_dir}\n"
    except Exception as e:
        result = f"Error: {str(e)}"

    return result
