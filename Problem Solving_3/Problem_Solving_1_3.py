number = int(input("Enter your number \n"))
Even_number = []
Odd_number = []
Sum_Even_Numbers = 0
Sum_odd_Numbers = 0
even_count = 0
odd_count = 0
The_Largest_Even_Number = 1
The_Largest_odd_Number = 1


for num in range(1, number + 1):

    if num % 2 == 0:
        if num > The_Largest_Even_Number:
            The_Largest_Even_Number = num
        even_count += 1
        Even_number.append(num)

    else:
        if num > The_Largest_odd_Number:
            The_Largest_odd_Number = num
        odd_count += 1
        Odd_number.append(num)
print("#" * 50)


print("Even".center(50, "-"))
print("#" * 50)
print(f"Even count={even_count}")
print(f"Sum_Even_Numbers ={sum(Even_number)}")
print(f"The_Largest_Even_Number = {The_Largest_Even_Number}")

print("#" * 50)
print("Odd".center(50, "-"))
print("#" * 50)
print(f"odd count = {odd_count}")
print(f"Sum_odd_Numbers ={sum(Odd_number)}")
print(f"The_Largest_odd_Number = {The_Largest_odd_Number}")
print("#" * 50)
