from functions.get_files_info import get_files_info
test_cases = [".", "pkg", "/bin", "../"]
for case in test_cases:
    info = get_files_info("calculator", case)
    print(info)