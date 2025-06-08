import os
from google.genai import types

def write_file(working_directory, file_path, content):
    full_path = os.path.join(working_directory, file_path)
    working_directory_path = os.path.abspath(working_directory)
    if not os.path.abspath(full_path).startswith(working_directory_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_path):
        if os.path.exists(full_path):
            return f'Error: File is not a regular file: "{file_path}"'
    path = os.path.dirname(full_path)
    os.makedirs(path, exist_ok=True)
    try:
        with open(full_path, "w") as f:
            f.write(content)
    
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: writing to file: {e}"
        
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes to the specified file. This will create a file if it does not exist in the specified location.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file, relative to the working directory"
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content that the file will be updated to after execution of the function"
            )
        },
        required=["file_path", "content"]
    )
)