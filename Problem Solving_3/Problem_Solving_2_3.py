start_num = int(input("Enter start num \n"))
end_num = int(input("Enter end num \n"))
total = 0
for num in range(start_num, end_num + 1):
    if num % 3 == 0 and num % 2 != 0:
        print(f"Found : {num}")
        total += num
print(f"Total : {total}")
