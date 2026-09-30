start_num = int(input("Enter start num \n"))
end_num = int(input("Enter end num \n"))
target_num = int(input("Enter the number to find its multiple\n"))

multiple_num = 0
multiple_sum = 0
multiple_count = 0
for num in range(start_num, end_num + 1):
    if num % target_num == 0:
        multiple_count += 1
        multiple_sum += num
        multiple_num = num
        print(f"{ multiple_num} is a multiple")


print(f"multiple_count= {multiple_count}")
print(f"multiple_sum = {multiple_sum}")
