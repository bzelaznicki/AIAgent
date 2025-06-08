import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    full_path = os.path.join(working_directory, file_path)
    working_directory_path = os.path.abspath(working_directory)
    if not os.path.abspath(full_path).startswith(working_directory_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(full_path):
            return f'Error: File "{file_path}" not found.'
    _, file_extension = os.path.splitext(file_path)
    if file_extension != ".py":
         return f'Error: "{file_path}" is not a Python file.'
    

    try:
        command = ["python3", full_path]

        if args:
             command.extend(args)

        result = subprocess.run(command, capture_output=True, text=True, timeout=30)

        output = []

        if result.stdout:
            output.append(f"STDOUT: {result.stdout}")
        if result.stderr:
            output.append(f"STDERR: {result.stderr}")
        
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output) if output else "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
     name="run_python_file",
     description="Runs a specified Python file. Will return the STDOUT, STDERR and return code if non 0",
     parameters=types.Schema(
          type=types.Type.OBJECT,
          properties={
               "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The path to the file, relative to the working_directory"
               ),
               "args": types.Schema(
                    type=types.Type.STRING,
                    description="An optional array of args to run the file with."
               )
          },
          required=["file_path"]
     )
)