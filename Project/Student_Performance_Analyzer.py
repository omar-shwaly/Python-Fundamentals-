student_count = int(input("Enter student_count\n"))
student = {}
Pass_count = 0
Fail_count = 0
The_Largest_Grade = 0
num = 0
while num < student_count:
    num += 1
    name = input("Enter your name\n")
    Grade = int(input("Enter your grades\n"))
    if Grade >= 90 and Grade <= 100:
        daegre = "Excellent"
    elif Grade >= 80 and Grade <= 89:
        daegre = "Very Good"
    elif Grade >= 70 and Grade <= 79:
        daegre = "Good"
    elif Grade >= 60 and Grade <= 69:
        daegre = "pass"
    elif Grade < 60 and Grade >= 0:
        daegre = "Fail"
    else:
        print("invlid Grade")

    student[name] = {"Grade": Grade, "daegre": daegre}
print(student)
for name in student:
    if student[name]["Grade"] >= 60:
        Pass_count += 1
    else:
        Fail_count += 1
    if student[name]["Grade"] > The_Largest_Grade:
        The_Largest_Grade = student[name]["Grade"]
        highest_student = name
        highest_daegre = student[highest_student]["daegre"]
print(f"Pass_count = {Pass_count}")
print(f"Fail_count = {Fail_count}")
print(
    f"The_highest_student = {highest_student} : Grade ={The_Largest_Grade}  daegre is :  {highest_daegre} "
)
