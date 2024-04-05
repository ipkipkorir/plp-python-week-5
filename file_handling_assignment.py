# writing to file
file_w = open("my_file.txt", "w")
file_w.write("Python file handling has 5 topics.\nThey are: \n1. File reading \n2. File writing \n3. File Appending \n4. File closing \n5. File Context Management")
file_w.close()

# reading from a file
file_r = open("my_file.txt", "r")
file_contents = file_r.read()
file_r.close()

# print the contents of the file
print(file_contents)

# appending to a file
file_a = open("my_file.txt", "a")
file_a.write("\n \nError handling has: \n1. Try \n2. Except \n3. Finally")
file_a.close()


# error handling
try:
    file = open("my_file.txt", "r")
    file_content = file.read()
    file.close()
except Exception as e:
    print("\nError: ")
    print(e)
    print()
else:
    print(file_content)



