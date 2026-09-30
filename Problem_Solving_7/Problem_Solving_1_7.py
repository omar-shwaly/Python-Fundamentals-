nums = [10, 80, 30, 40, 50, 60]
iterator = iter(nums)

try:

    number = next(iterator)
    if number >= 30:
        print(number)

    number = next(iterator)
    if number >= 30:
        print(number)

    number = next(iterator)
    if number >= 30:
        print(number)

    number = next(iterator)
    if number >= 30:
        print(number)

    number = next(iterator)
    if number >= 30:
        print(number)

    number = next(iterator)
    if number >= 30:
        print(number)

except StopIteration:
    print("Iterator finished")
