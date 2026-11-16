def menu():
    print("#" * 50)
    print("menu".center(50, "-"))
    print("#" * 50)
    print("1- Student Management")
    print("2- Grade Management")
    print("3- Task Management")
    print("4- Reports")
    print("5- Exit")
    print("#" * 50)


def student_management():

    choose = 0
    while choose != 5:

        print("You selected :  Student Management ")
        print("#" * 50)
        print(" Student Management menu".center(50, "-"))
        print("#" * 50)
        print("1- Add student")
        print("2-View Students")
        print("3- Search Student")
        print("4- Delete Student")
        print("5- Exit")
        print("#" * 50)

        try:
            choose = int(input("Enter your  choose\n"))
        except ValueError:
            print("invalid input Enter your choose agin ")

        if choose == 1:
            print("You selected : Add student ")
            name_student = input("Enter your name \n").strip()
            if name_student:
                with open(
                    "Python_1/python_Final_Capston_Project/student_management.txt",
                    "a",
                    encoding="utf-8",
                ) as file:
                    file.write(name_student + "\n")
                    print("Student Added Successfuly")
            else:
                print("name cannot be empthy")

        elif choose == 2:
            print("You selected : View Students")
            with open(
                "Python_1/python_Final_Capston_Project/student_management.txt",
                "r",
                encoding="utf-8",
            ) as file:
                lines = file.readlines()
                for line in lines:
                    if lines:
                        print(line.strip())
                    else:
                        print("The student file is empthy")

        elif choose == 3:
            print("You selected : Search")
            search_name = input("Enter your search name \n")
            with open(
                "Python_1/python_Final_Capston_Project/student_management.txt",
                "r",
                encoding="utf-8",
            ) as file:

                lines = file.readlines()
                for line in lines:
                    if search_name.lower() in line.lower():
                        print(f"Found : {line.strip()}")
                    else:
                        print(f"Not Found {search_name}")

        elif choose == 4:
            print("You selected :Delete Student ")
            delete_name = input("Enter the name you wish to delete \n")
            with open(
                "Python_1/python_Final_Capston_Project/student_management.txt",
                "r",
                encoding="utf-8",
            ) as file:
                lines = file.readlines()
            with open(
                "Python_1/python_Final_Capston_Project/student_management.txt",
                "w",
                encoding="utf-8",
            ) as file:
                for line in lines:
                    if delete_name.lower() not in line.lower():
                        file.write(line)

        elif choose == 5:
            print("You selected : Exit")
            print("Reaturning to Main menu ")
            break

        else:
            print("Invalid choose")


def grade_management():
    print("You selected : grade management  ")
    choice = 0
    while choice != 7:
        print("#" * 50)
        print("grade_management".center(50, "-"))
        print("#" * 50)
        print("1- Add Grade")
        print("2- View Grades")
        print("3- Search Student Grades")
        print("4- Calculate Average")
        print("5- Show Highest Grade")
        print("6- Show Lowest Grade")
        print("7- Exit")
        print("#" * 50)

        try:
            choice = int(input("Enter your choice\n"))
        except ValueError:
            print("Invalid input! please enter the choice number")

        if choice == 1:
            print("You selected : Add Grade ")
            name = input("Enter student name \n").strip()
            try:
                grade = int(input("Enter grade student\n"))

                with open(
                    "Python_1/python_Final_Capston_Project/grade_management.txt",
                    "a",
                    encoding="utf-8",
                ) as file:

                    file.write(f"{name} : {grade} \n")

                print("Grade Addded Successfully")

            except ValueError:
                print("the grade must be an integar")

        elif choice == 2:
            print("You selected : View Grades ")
            with open(
                "Python_1/python_Final_Capston_Project/grade_management.txt",
                "r",
                encoding="utf-8",
            ) as file:

                lines = file.readlines()

                if line:
                    for line in lines:
                        print("Grade list".center(50, "-"))
                        print(line.strip())
                else:
                    print("No grade recorded")

        elif choice == 3:
            print("You selected : Search Student Grades ")
            search_name = input("Enter Searsh Student Name\n").strip()
            with open(
                "Python_1/python_Final_Capston_Project/grade_management.txt",
                "r",
                encoding="utf-8",
            ) as file:

                lines = file.readlines()

                for line in lines:
                    if search_name.lower() in line.lower():
                        print(f"{line.strip()}")
                    else:
                        print("not found grade student")

        elif choice == 4:

            print("You selected : Calculate Average ")

            with open(
                "Python_1/python_Final_Capston_Project/grade_management.txt",
                "r",
                encoding="utf-8",
            ) as file:
                lines = file.readlines()

            grades = []
            for line in lines:
                if ":" in line:
                    parts = line.strip().split(":")

                    try:
                        grade = float(parts[1].strip())
                        grades.append(grade)

                    except ValueError:
                        continue

                    if grades:
                        average = sum(grades) / len(grades)
                        print(f"Average grades student = {average:.2f}")

                    else:
                        print("No grades recorded to calculate the average")

        elif choice == 5:

            print("You selected :Show The Highest Grade")

            with open(
                "Python_1/python_Final_Capston_Project/grade_management.txt",
                "r",
                encoding="utf-8",
            ) as file:
                lines = file.readlines()

                highest_grade = -1
                top_student = ""

                for line in lines:
                    if ":" in line:
                        parts = line.strip().split(":")
                        student_name = parts[0].strip()

                        try:
                            grade = float(parts[1].strip())
                            if grade > highest_grade:
                                highest_grade = grade
                                top_student = student_name
                        except ValueError:
                            continue
                    if top_student:
                        print(
                            f"Highest grade = {highest_grade} top student name :   {top_student}"
                        )
                    else:
                        print("Not Found recordded grades")

        elif choice == 6:
            print("You selected : Show The Lowest Grade")

            with open(
                "Python_1/python_Final_Capston_Project/grade_management.txt",
                "r",
                encoding="utf-8",
            ) as file:
                lines = file.readlines()
                lowest_grade = 1000
                lowst_student = ""

                for line in lines:
                    if ":" in line:
                        parts = line.strip().split(":")
                        student_name = parts[0].strip()
                        try:
                            grade = float(parts[1].strip())
                            if grade < lowest_grade:
                                lowest_grade = grade
                                lowst_student = student_name
                        except ValueError:
                            continue

                    if lowst_student:
                        print(
                            f" The Lowest  grade ={ lowest_grade}  Lowest student name :{lowst_student}"
                        )

                    else:
                        print("Not Found recorded grades")

        elif choice == 7:

            print("You selected : Exit")
            print("Reaturning to Main menu ")
            break

        else:
            print("Invalid choice")


def task_management():
    print("You selected : task management ")
    select = 0
    while select != 5:
        print("#" * 50)
        print("Task management".center(50, "-"))
        print("#" * 50)
        print("1- Add task")
        print("2- View taskes")
        print("3- Search task")
        print("4- Delete task")
        print("5- Exit")

        try:
            select = int(input("Enter your selection \n"))
        except ValueError:
            continue

        if select == 1:
            print("You selected :  Add task")

            task = input("Enter your task \n")
            with open(
                "Python_1/python_Final_Capston_Project/task_management.txt",
                "a",
                encoding="utf-8",
            ) as file:
                file.write(task + "\n")

        elif select == 2:
            print("You selected : View taskes ")
            with open(
                "Python_1/python_Final_Capston_Project/task_management.txt",
                "r",
                encoding="utf-8",
            ) as file:
                lines = file.readlines()

                for line in lines:
                    if line:
                        print(line.strip())
                    else:
                        print("not found recorded tasks")

        elif select == 3:
            print("You selected :  Search task")
            with open(
                "Python_1/python_Final_Capston_Project/task_management.txt",
                "r",
                encoding="utf-8",
            ) as file:
                lines = file.readlines()
                search_about_task = input("Enter the task you wish to find\n").strip()
                for line in lines:
                    if search_about_task.lower() in line.lower():
                        print(f"Found The Searched task : {line.strip()}")
                    break
                else:
                    ("The requested task was not found")

        elif select == 4:
            print("You selected : Delete task  ")
            with open(
                "Python_1/python_Final_Capston_Project/task_management.txt",
                "r",
                encoding="utd-8",
            ) as file:
                lines = file.readlines()
                num = 1
                for line in lines:
                    print(f"{num}- {line}")

                number_task_delete = int(input("Enter number  task dlate\n"))
            with open(
                "Python_1/python_Final_Capston_Project/task_management.txt",
                "w",
                encoding="utd-8",
            ) as file:

                if num != number_task_delete:
                    file.write(line)
                num += 1
                print("Task deleted successfully")

        elif select == 5:
            print("You selected : Exit")
            print("Reaturning to Main menu ")
            break


def reports():

    print("You selected : Reports")

    Decision = 0
    while Decision != 2:

        print("#" * 50)
        print("Reports".center(50, "-"))
        print("#" * 50)
        print("1- Full Academic Report")
        print("2- Exit")
        print("#" * 50)

        try:
            Decision = int(input("Enter your Decision\n"))
        except ValueError:

            continue

        if Decision == 1:
            print("#" * 50)
            print("Full Academic Report".center(50, "-"))
            print("#" * 50)
            print("Studnt".center(50, "-"))
            print("#" * 50)
            with open(
                "Python_1/python_Final_Capston_Project/student_management.txt",
                "r",
                encoding="utf-8",
            ) as file:
                lines = file.readlines()
            total_student = 0
            for line in lines:
                if line.strip():
                    total_student += 1
            if total_student > 0:
                print(f"Total Student :{ total_student} ")
                print("#" * 50)
            else:
                print("No students found in the file")

            print("Grades".center(50, "-"))
            print("#" * 50)

            Student_with_grade = []
            passed = 0
            failed = 0
            with open(
                "Python_1/python_Final_Capston_Project/grade_management.txt",
                "r",
                encoding="utf-8",
            ) as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(":")

                    if len(parts) >= 2:

                        try:
                            grade = float(parts[1].strip())
                            Student_with_grade.append(grade)
                            if grade >= 60 and grade <= 100:
                                passed += 1
                            elif grade < 60 and grade >= 0:
                                failed += 1

                        except ValueError:
                            print(f"Invalid grade valu : {line}")
                    else:
                        print(f"not found grade in line : {line}")

            print(f"Student_with_grade : {len(Student_with_grade)}")
            print(f"Student passed : {passed}")
            print(f"student failed : {failed}")
            print("#" * 50)
            print("Tasks".center(50, "-"))
            print("#" * 50)

            with open(
                "Python_1/python_Final_Capston_Project/task_management.txt",
                "r",
                encoding="utf-8",
            ) as file:
                lines = file.readlines()
            Total_tasks = 0
            for line in lines:
                if line.strip():
                    Total_tasks += 1

            if Total_tasks > 0:
                print(f"Total tasks = {Total_tasks}")
                print("#" * 50)

            else:
                print("Not found recorded task")

        elif Decision == 2:

            print("You selected : Exit")
            print("Reaturning to Main menu ")
            break


def exit():
    print("You selected : Exit")
    print("Goodbye!")


option = 0
while option != 5:
    menu()

    option = int(input("Enter your option\n"))
    if option == 1:
        student_management()

    elif option == 2:
        grade_management()

    elif option == 3:
        task_management()

    elif option == 4:
        reports()

    elif option == 5:
        exit()
