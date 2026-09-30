with open("File/student.txt", "r") as file:
    for line in file:
        print(f"student : {line}".strip())
