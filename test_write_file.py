from functions.write_file import write_file
test_cases = {
    "lorem.txt":"wait, this isn't lorem ipsum",
    "pkg/morelorem.txt":"lorem ipsum dolor sit amet",
    "/tmp/temp.txt":"this should not be allowed"}
for key,value in test_cases.items():
    wrote = write_file("calculator", key,value)
    print(wrote)