import os


def get_files_info(working_directory, directory="."):
    try:
        abspath_wd = os.path.abspath(working_directory)
        full_path = os.path.join(abspath_wd, directory)
        abspath_d = os.path.abspath(full_path)
        if not abspath_d.startswith(abspath_wd):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'

        files = os.listdir(full_path)
        result = ""
        file_size = 0
        for file in files:
            path = os.path.join(full_path, file)
            is_dir = not os.path.isfile(path)
            file_size = os.path.getsize(path)
            result += f" - {file}: file_size:{file_size} bytes, is_dir={is_dir}\n"
    except Exception as e:
        result = f"Error: {str(e)}"

    return result
