import os
import config
def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        abs_working_dir:str = os.path.abspath(working_directory)
        joined:str = os.path.join(abs_working_dir,file_path)
        target:str = os.path.abspath(joined)
    

        valid_target_dir:bool = os.path.commonpath([abs_working_dir, target]) == abs_working_dir
        if not valid_target_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target):
            return f'Error: File not found or is not a regular file: "{file_path}"'
    
        with open(target,"r") as f:
            
            file_content_string = f.read(config.MAX_CHARS)

            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {config.MAX_CHARS} characters]'
            return file_content_string
    
    except Exception as e:
        return f"Error: {e}"