random_number_List = []
random_number = 0
Largest_number = 0
Lowest_number = 100
sum_numbers = 0
Average_numbers = 0


from random import randint

for n in range(5):
    random_number = randint(1, 100)
    random_number_List.append(random_number)
print(random_number_List)


for num in random_number_List:
    sum_numbers += num
    if num > Largest_number:
        Largest_number = num
    if num < Lowest_number:
        Lowest_number = num
print(f"The Largest number in random number List = {Largest_number} ")
print(f"The lowest number in random number list = {Lowest_number}")
print(
    f"The Average is numbers in random number list = { sum_numbers/len(random_number_List)}"
)
