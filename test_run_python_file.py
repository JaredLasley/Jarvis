from functions.run_python_file import run_python_file
test_cases:list[tuple[str,str, list[str]| None]] = [
    ("calculator","main.py", None),
    ("calculator", "main.py", ["3 + 5"]),
    ("calculator", "tests.py", None),
    ("calculator", "../main.py", None),
    ("calculator", "nonexistent.py", None),
    ("calculator", "lorem.txt", None)]
for directory,path,arg in test_cases:
    result = run_python_file(directory,path ,arg)
    print(f"Running: {directory}/{path} with args={arg}")
    print(result)
    print("---")