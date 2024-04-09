def build_new_number(number1, number2):  # Ex.9
    new_number = 0
    multiply = 1
    while number1 != 0:
        digit1 = number1 % 10
        digit2 = number2 % 10
        for x in range(digit1):
            if new_number >= 100000000:
                return new_number
            new_number += digit2 * multiply
            multiply *= 10
        number1 //= 10
        number2 //= 10
    return new_number


def reverse_number(number):  # reverse the order of digits in number
    reversed_number = 0
    while number != 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
    return reversed_number


def divide_and_reverse(number, digit):  # Ex.10
    new_number = 0
    multiply = 1
    parts_len = 10 ** digit
    while number != 0:
        parts = number % parts_len
        parts = reverse_number(parts)
        new_number += parts * multiply
        multiply *= parts_len
        number //= parts_len
    return new_number


def sand_clock(base, symbol):  # Ex. 13
    for i in range(-base, base + 1):
        if i != 0:
            print(" " * (base - abs(i)) + f"{symbol} " * (abs(i)))


def triangle(base, symbol):
    spaces = base - 1
    res = " " * spaces
    for i in range(1, base + 1):
        for j in range(i):
            res += f"{symbol} "
        spaces -= 1
        if spaces >= 0:
            res += "\n" + " " * spaces
    return res


def tree(base, symbol):  # Ex.15
    tree = ""
    for i in range(3):
        tree += triangle(base, symbol) + "\n"
    for i in range(base):
        tree += " " * (base - 1) + f"{symbol}\n"
    return tree


def mates(number):  # Ex.16
    res = ""
    count = 0
    num = 220
    while count < number:
        sum = 0
        sum2 = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        for i in range(1, sum):
            if sum % i == 0:
                sum2 += i
        if sum2 == num and num < sum:
            count += 1
            res += f"{num} and {sum} are mates\n"
        num += 1
    return res


def menu():
    choice = input("what question would you like to solve?\nfor exit type: EXIT\n")
    while choice != "EXIT":
        if choice == "9":
            num1 = int(input("enter the first number: "))
            num2 = int(input("enter the second number: "))
            print(f"the new number is {build_new_number(num1, num2)}")
        elif choice == "10":
            num = int(input("enter number: "))
            digit = int(input("enter digit: "))
            print(f"the new number is {divide_and_reverse(num, digit)}")
        elif choice == "13":
            base = int(input("enter the the sand clock base: "))
            symbol = input("enter the symbol to create the clock: ")
            print(sand_clock(base, symbol))
        elif choice == "15":
            base = int(input("enter the triangle base: "))
            symbol = input("enter the symbol to create the tree")
            print(tree(base, symbol))
        elif choice == "16":
            number = int(input("enter how many mates would you like to get: "))
            print(mates(number))
        else:
            print("wrong input try again")
        choice = input("what question would you like to solve?\nfor exit type: EXIT\n")


menu()
