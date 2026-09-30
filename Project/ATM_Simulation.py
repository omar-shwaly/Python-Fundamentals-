balance = 10000
option = 0
while option != 4:

    print("#" * 50)
    print("menu".center(50, "-"))
    print("1-check balance ")
    print("2-Deposit ")
    print("3-withddraw")
    print("4-Exit")
    print("#" * 50)

    option = int(input("Enter Your option\n"))

    if option == 1:
        print("You selected : check balance")
        print(f"Current balance = {balance}")

    elif option == 2:
        print("You selected : Deposit")
        Deposit_amount = float(input("Enter  Deposit_amount\n"))
        if Deposit_amount > 0:
            balance += Deposit_amount
            print(f" Successfully deposited  New balance  ={balance}")
        else:
            print("Deposit_amount must be positive")

    elif option == 3:
        print("You selected : withdraw")

        withdraw_amount = float(input(" withdraw_amount\n"))
        if withdraw_amount <= 0:
            print("  withdraw_amount must be positive")

        elif withdraw_amount < balance:
            print("insufficient balance")

        else:
            balance -= withdraw_amount
            print(f" Successfully withddrawn New balance ={balance}")

    elif option == 4:
        print("Goodbye!")

    else:
        print("invalid option ! pleas select 1,2,3 or 4.")
