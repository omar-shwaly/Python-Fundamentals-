option = 0
while option != 3:

    print("#" * 50)
    print("menu".center(50, "-"))
    print("#" * 50)
    print("1-Add Note")
    print("2-View Notes")
    print("3-Exit")
    print("#" * 50)

    option = int(input("Enter your opthion\n"))

    if option == 1:

        print("You selected : Add Note")
        with open("File/note.txt", "a", encoding="utf-8") as file:
            note_add = input("Enter your note\n")
            file.write(note_add + "\n")
            print("Successfully Add note \n")

    elif option == 2:
        print("You selected :View Notes")
        with open("File/note.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()
        if len(lines) == 0:
            print("Not found note\n")
        else:
            for line in lines:
                print(line, end="")
            print()

    elif option == 3:
        print("You selected :Exit")
        print("Godbay!")
    else:
        print("Invalid option! plase select 1 or 2 or 3 ")
