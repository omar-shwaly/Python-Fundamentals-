def even_numbers():
    start_number = int(input("Enter your start number \n"))
    end_number = int(input("Enter your end number \n"))
    even_numbers = []

    for num in range(start_number, end_number + 1):
        if num % 2 == 0:
            even_numbers.append(num)
    print(even_numbers)


even_numbers()
