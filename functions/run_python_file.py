import subprocess
import os
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the contents of a specified file within the working directory with or without additional arguments",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to target file, relative to the working directory (default is the working directory itself)",
            ),
         "args": types.Schema(
                type=types.Type.ARRAY,
                description="Additional arguments to be used when running the program",
                items=types.Schema(
                    type=types.Type.STRING,
                    
                )
            ),
        },
        required=["file_path"],
    ),
)

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target = os.path.normpath(os.path.join(abs_working_dir,file_path))

        #checking for file path inclusion in cwd
        if os.path.commonpath([abs_working_dir,target]) != abs_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        #create the command to be run in a list, add args if they exist
        command = ["python", target]
        if args:
            command.extend(args)
        #run the command in subprocess

        complete = subprocess.run(command,
            cwd=abs_working_dir,
            capture_output=True,
            text=True,
            timeout=30)
        #create the stdout and stderr objects as well as the return string
        result = complete.stdout
        error1 = complete.stderr
        outtext:str =""
        #return code printing control logic
        if complete.returncode != 0:
            outtext += f"Process exited with code {complete.returncode}"
        if not result and not error1:
            if outtext =="":
                outtext += "No output produced"
            else:
                outtext += "\n No output produced"
            return outtext
        else:
            if outtext =="":
                outtext += f"STDOUT: {result}\nSTDERR: {error1}"
            else:
                outtext += f"\nSTDOUT: {result}\nSTDERR: {error1}"
            return outtext
    #exception handling
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
    