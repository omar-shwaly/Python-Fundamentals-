def menu():
    print("#" * 50)
    print("menu".center(50, "-"))
    print("#" * 50)
    print("1- add two number ")
    print("2 - subtract two number ")
    print("3- mult two number")
    print("4-devided two number")
    print("5- Exit")
    print("#" * 50)


def add(number_1, number_2):
    result = number_1 + number_2
    print(f"Addition number_1 + number_2 = {result}")


def sub(number_1, number_2):
    result = number_1 - number_2
    print(f"Subtraction number_1 - number_2 = {result}")


def mult(number_1, number_2):
    result = number_1 * number_2
    print(f"multiblation number_1 * number_2 = {result}")


def devided(number_1, number_2):
    result = number_1 / number_2
    print(f"devided number_1 / number_2 = {result}")


try:

    number_1 = int(input("Enter your number_1\n"))
    number_2 = int(input("Enter your number _2\n"))

    option = 0
    while option != 5:

        menu()
        option = int(input("Enter your option \n"))

        if option == 1:
            add(number_1, number_2)

        elif option == 2:
            sub(number_1, number_2)

        elif option == 3:
            mult(number_1, number_2)

        elif option == 4:
            devided(number_1, number_2)

        elif option == 5:
            print("Godbay!")

        else:
            print("Invalid number plase enter number from 1 to 5")


except ValueError:
    print("plase enter invalid number")

except ZeroDivisionError:
    print("cannot devide by zero")
