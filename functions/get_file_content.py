import os
from google.genai import types

from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    full_path = os.path.join(working_directory, file_path)
    working_directory_path = os.path.abspath(working_directory)
    if not os.path.abspath(full_path).startswith(working_directory_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
   

    with open(full_path, "r") as f:
        file_content_string = f.read(MAX_CHARS)
        if len(file_content_string) == MAX_CHARS:
            file_content_string += f'\n[...File "{file_path}" truncated at 10000 characters]'

    return file_content_string


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the file content in a specified file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file, relative to the working_directory."
            )
        },
        required=["file_path"]
    )
)
