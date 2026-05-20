from functions.get_file_content import get_file_content

result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")

test_cases = ["main.py", "pkg/calculator.py", "/bin/cat", "pkg/does_not_exist.py"]

for case in test_cases:
    print(get_file_content("calculator", case))
