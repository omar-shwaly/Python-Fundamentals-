student_count = 0
sum_grade = 0
Average_grade = 0
highest_grade = 0
highest_student = ""
highest_Rating = ""

Lowest_grade = 100
Lowest_student = ""
Lowest_Rating = ""


with open("File/Students.txt", "r") as file:
    Lines = file.readlines()
    for Line in Lines:
        data = Line.strip().split(",")
        student_count += 1
        # print(data)
        name = data[0]
        grade = int(data[1])

        if grade >= 90 and grade <= 100:
            Rating = "Excellent"

        elif grade >= 80 and grade <= 89:
            Rating = "Very Good"

        elif grade >= 70 and grade <= 79:
            Rating = "Good"
        elif grade >= 60 and grade <= 69:
            Rating = "pass"
        elif grade < 60 and grade >= 0:
            Rating = "Fail"
        else:
            print("invalid Grade")

        if grade > highest_grade:
            highest_grade = grade
            highest_student = name
            highest_Rating = Rating

        if grade < Lowest_grade:
            Lowest_grade = grade
            Lowest_student = name
            Lowest_Rating = Rating

        sum_grade += grade
        print(f"Name is : {name} , Grade = { grade} Rating is : {Rating}  ")

if student_count > 0:
    Average_grade = sum_grade / student_count
print(f"student_count = {student_count} ")
print(f"Average_grade = {Average_grade}")
print(
    f"The Highest Student is : { highest_student} : Grade ={ highest_grade} : Rating is : {highest_Rating}"
)

print(
    f"The  Lowest student  is : {  Lowest_student} : Grade ={  Lowest_grade} : Rating is : {Lowest_Rating }"
)
print("")
