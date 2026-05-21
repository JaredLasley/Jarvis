#imports
import os

#function creation
def write_file(working_directory: str, file_path: str, content: str) -> str:
    
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target = os.path.normpath(os.path.join(abs_working_dir,file_path))

        #checking for file path inclusion in cwd
        if os.path.commonpath([abs_working_dir,target]) != abs_working_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        #check existence of directories and create missing directories
        os.makedirs(os.path.dirname(target),exist_ok=True)
        
        #open file in write mode
        with open(target, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
