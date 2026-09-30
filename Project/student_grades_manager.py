student = {
    "Omar": {"grades": [90, 85, 78]},
    "Ahmed": {"grades": [70, 80, 65]},
    "Ali": {"grades": [95, 88, 100]},
}


option = 0

while option != 7:

    print("#" * 50)
    print("menio")
    print("#" * 50)

    print("Student Grades Maager ")
    print("-" * 50)
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Show Student Average")
    print("4. Show Highest Average")
    print("5. Show Passed Students")
    print("6. Show Unique Grades")
    print("7. Exit")
    print("#" * 50)

    option = int(input("Please select an option \n"))

    if option == 1:

        print("You selected : Add Student")

        choose = input("Would you like to add student y/n \n")

        if choose == "y":

            name = input("Enter your name  \n")

            grades = list(map(int, input("Enter your grades ").split()))

            student[name] = {"grades": grades}

            print(student)

        else:

            print("Ok")
            option = int(input("Please select an option agin \n"))

    elif option == 2:
        print("You selected : Show All Students")
        print(f"the all stuent {student}")

    elif option == 3:
        print("You selected : Show Student Average")

        name = input("Enter Your name \n").capitalize()

        grades = student[name]["grades"]

        Average = sum(grades) / len(grades)

        print(f"Average is : {Average}")

    elif option == 4:

        print("You selected : Show Highest Average")

        highest_Average = 0

        highest_student = ""

        for name in student:

            grades = student[name]["grades"]

            Average = sum(grades) / len(grades)

            if Average > highest_Average:
                highest_Average = Average
                highest_student = name

        print(highest_Average)
        print(highest_student)

    elif option == 5:
        print("You selected : Show Passed Students")
        for name in student:
            grades = student[name]["grades"]
            Average = sum(grades) / len(grades)

            if Average >= 60:
                student_passed = name
                print(student_passed)

    elif option == 6:
        print("You selected : Show Unique Grades")

        unique_grades = set()

        for name in student:
            grades = student[name]["grades"]
            for grade in grades:
                unique_grades.add(grade)
        print(unique_grades)

    elif option == 7:

        print("Goodbye!")
