Grade = int(input("Enter Your Grade \n"))

if Grade >= 90 and Grade <= 100:
    print("Excellent")

elif Grade >= 80 and Grade <= 89:
    print("Very Good")

elif Grade >= 70 and Grade <= 79:
    print("Good")

elif Grade >= 60 and Grade <= 69:
    print("Pass")

elif Grade < 60 and Grade >= 0:
    print("Fail")


else:
    print("Invalid Grade")
