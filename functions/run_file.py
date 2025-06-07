import os
import subprocess

def run_python_file(working_directory, file_path):
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

        result = subprocess.run(command, capture_output=True, text=True, timeout=30)

        output = []

        if result.stdout:
            output.append(f"STDOUT: {result.stdout}")
        if result.stderr:
            output.append(f"STDERR: {result.stderr}")
        
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output) if output else "No output produced."
    except:
        return f"Error: executing Python file: {e}"