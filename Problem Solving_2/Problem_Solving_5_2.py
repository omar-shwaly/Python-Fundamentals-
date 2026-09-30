user_name = "admin"
password = 1234

username = input("Enter user_name \n").lower()

pa_ssword = int(input("Enter password\n"))

if username == user_name:

    print("valid username ")

    if password == pa_ssword:

        print("valid password")
        print("Log in successfull")

    else:
        print("invalid password")
else:
    print(" invalid username ")
