name= input("Enter Your name \n :")
age= int(input("Enter your age \n :"))
city=input("Enter your city \n :")
Favorite_Subject=input("Enter Your Favorite Subject \n :")
Physics_grade=int(input("Enter your Physics grade \n :"))
Chemistry_grade=int(input("Enter your Chemistry grade \n :"))
Biology_grade=int(input("Enter your  grade Biology \n :"))



Total_grades = Biology_grade + Chemistry_grade + Physics_grade
Average_grades= Total_grades / 3


gradae_list=[Physics_grade , Physics_grade , Biology_grade , Total_grades , Average_grades]


Student_data = {
"name" : name ,
"age" : age ,
"city" : city ,
"Favorite_Subject" : Favorite_Subject ,
"grades":gradae_list  ,
"Total_grades": Total_grades ,
"Average_grades":Average_grades
}

subject= (Physics_grade , Chemistry_grade  , Biology_grade )

subject_set= set(subject)

print(subject_set)
print(type(subject_set))


print("Information Report student ".center(90,"#"))


#print(f"Student name is :{name}")
#print(f"Student age is :{age}")
#print(f"Student housing is :{city}")
#print(f" The Favorite_Subject :{Favorite_Subject}")

print(type(Student_data))
print(Student_data)

print(subject)

print(f"The First letter of the name : {name[0]}")
print(f"Thelast letter of the name : {name[-1]}")

print(f" of letters in the name :{len(name)}")


print(name .upper())