import os
from google.genai import types


def get_files_info(working_directory, directory=None):
    try:
        full_path = os.path.join(working_directory, directory)
        working_directory_path = os.path.abspath(working_directory)
        if not os.path.abspath(full_path).startswith(working_directory_path):
            return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'
    

        directory_files = os.listdir(full_path)
        directory_arr = []
        for file in directory_files:
            file_location = os.path.join(full_path, file)
            file_size = 0
            is_dir = os.path.isdir(file_location)
            if not is_dir:
                file_size = os.path.getsize(file_location)
            directory_arr.append(f"- {file}: file_size={file_size} bytes, is_dir={is_dir}")

        return "\n".join(directory_arr)
    except Exception as e:
        return f"Error: {str(e)}"
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)