days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Sunday"]
day = ""


def menu():
    print("#" * 50)
    print("Menu".center(50, "-"))
    print("#" * 50)
    print("1- Add task")
    print("2- View tasks")
    print("3- Dlete task")
    print("4- Exit")
    print("#" * 50)


def Add_Task():
    day = input("Enter your day \n").strip().capitalize()
    if day in days:
        with open("Python_1/File/Tasks.txt", "a", encoding="utf-8") as file:
            file.write(f" {day}".center(20, "*") + "\n")

            while True:
                tasks = input("Enter your tasks (or -1 to stop): ".strip() + "\n")

                if tasks == "-1":
                    print("Finished adding tasks.")
                    break
                file.write(tasks + "\n")
                print("Task Added Successfuly")
    else:
        print("Invalid day")


def View_Tasks():

    with open("Python_1/File/Tasks.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        if len(lines) == 0:
            print("Not found task")
        else:
            for line in lines:
                print(line.strip())


def Dlete_Task():
    with open("File/Tasks.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        print(f"{i+1} - {lines[i].strip()}")
    num = int(input("Enter task number to delete \n"))
    lines.pop(num - 1)
    with open("Python_1/File/Tasks.txt", "w", encoding="utf-8") as file:
        file.writelines(lines)
    print("Task Deleted Successfuly")


def Exit():
    print("Goodbye!")


option = 0
while option != 4:
    menu()
    option = int(input("Enter your option \n"))
    if option == 1:
        Add_Task()
    elif option == 2:
        View_Tasks()
    elif option == 3:
        Dlete_Task()
    elif option == 4:
        Exit()
    else:
        print("Invalid option Enter number from 1 to 4")
