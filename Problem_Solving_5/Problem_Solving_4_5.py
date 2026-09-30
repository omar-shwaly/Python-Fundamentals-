matching_lines = 0

search_word = input("Enter your The word you want to search for \n")
with open("File/messages.txt", "r") as file:

    for line in file:

        if search_word.lower() in line.lower():
            matching_lines += 1

            print(line.strip())
            print(f"Number Of Lines Countaining The Word Input = {matching_lines}")
