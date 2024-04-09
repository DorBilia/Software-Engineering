def numbers_to_list(n=3):
    arr = []
    for i in range(n):
        num = int(input("enter a number"))
        arr.append(num)
    return arr


def sum_of_list(numbers):
    sum_numbers = 0
    for i in numbers:
        sum_numbers = sum_numbers + i
    return sum_numbers


def reverse(list):
    new_list = []
    for i in range(len(list) - 1, -1, -1):
        new_list.append(list[i])
    print(new_list)


