def add(num_1, num_2):
    result = num_1 + num_2
    print(f"addetion 2 number =  {result}")


def subtract(num_1, num_2):
    result = num_1 - num_2
    print(f"subtraction 2 number =  {result}")


def multiply(num_1, num_2):
    result = num_1 * num_2
    print(f"amultiplition 2 number =  {result}")


def divide(num_1, num_2):
    result = num_1 / num_2
    if num_2 == 0:
        print("Zero_Division_Error")
    else:
        print(f"divided 2 number =  {result}")


option = 0
while option != 5:

    print("#" * 50)
    print("menu".center(50, "-"))
    print("#" * 50)
    print("1- add two number")
    print("2- sutract two number")
    print("3- multibly two number")
    print("4- devide two number")
    print("5- Exit")
    print("#" * 50)

    option = int(input("Enter your option\n"))
    if option == 5:
        print("You selected :  Exit ")
        print("Goodbye!")

    elif option in [1, 2, 3, 4]:

        num_1 = int(input("Enter your number_1 \n"))
        num_2 = int(input("Enter your number_2 \n"))

        if option == 1:
            print("You selected :addetion")
            add(num_1, num_2)

        elif option == 2:
            print("You selected :subtraction")
            subtract(num_1, num_2)

        elif option == 3:
            print("You selected : amultiplition")
            multiply(num_1, num_2)

        elif option == 4:
            print("You selected : Division ")
            divide(num_1, num_2)

    else:
        print(" Invalid option ! palse entar anumber from 1 to 5")
