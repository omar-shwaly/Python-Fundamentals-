start_num = int(input("Enter start num \n"))
end_num = int(input("Enter end num \n"))
even_count = 0
even__sum = 0
odd_count = 0
for num in range(start_num, end_num + 1):
    if num % 2 == 0:
        even_count += 1
        even__sum += num

    else:
        odd_count += 1
print(f"even_count = {even_count}")
print(f"odd_count = {odd_count}")
print(f"even_sum = {even__sum}")
