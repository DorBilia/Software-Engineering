import XOGame


# Ex.13
def col_of_stars(lst):
    max_num = max(lst)
    for i in range(max_num, 0, -1):
        for j in lst:
            if j >= i:
                print('*', end='')
            else:
                print(' ', end='')
            print(' ', end='')
        print()
    for j in lst:
        print(j, end=' ')
    return ""


# Ex.14
def add(lst1, lst2):
    res = []
    rem = 0  # the 1 we need to remember if the sum of 2 digits is >=10
    if len(lst1) > len(lst2):
        bigger_lst = lst1
        smaller_lst = lst2
    else:
        bigger_lst = lst2
        smaller_lst = lst1
    index = min(len(lst2), len(lst1))
    for i in range(len(bigger_lst) - 1, -1, -1):
        if index > 0:
            sum_of_col = bigger_lst[i] + smaller_lst[index - 1] + rem
            if sum_of_col >= 10:
                rem = 1
                res.append(sum_of_col % 10)
            else:
                rem = 0
                res.append(sum_of_col)
            index -= 1
        else:
            sum_of_col = bigger_lst[i] + rem
            if sum_of_col >= 10:
                rem = 1
                res.append(sum_of_col % 10)
            else:
                rem = 0
                res.append(sum_of_col)
    if rem == 1:
        res.append(1)
    return res[::-1]


# Ex.16
def num_len(num):
    count = 0
    while num != 0:
        count += 1
        num //= 10
    return count


def divide_number(num):
    length = num_len(num)
    side = 0
    multi = 1
    if length % 2 == 0:
        flag = 0
    else:
        flag = 1
    for i in range(length // 2 + flag):
        side += (num % 10) * multi
        multi *= 10
        num //= 10
    return [side, num]


def is_kaprekar_without_strings(num):
    new_num = num * num
    sides = divide_number(new_num)
    if sides[0] + sides[1] == num:
        return f"true {sides}"
    return f"false {[]}"


def is_kaprekar_with_strings(num):
    new_num = str(num * num)
    sides = []
    if len(str(new_num)) % 2 == 0:
        flag = 0
    else:
        flag = 1
    side1 = int(new_num[:len(new_num) // 2])
    side2 = int(new_num[len(new_num) // 2 + flag:])
    if side1 + side2 == num:
        sides.append(side1)
        sides.append(side2)
        return f"true {sides}"
    return f"false {sides}"


# Ex.3
def fill_col(matrix, index, value, direction):
    if direction:
        for i in range(len(matrix)):
            matrix[i][index] = value
            value += 1
    else:
        for i in range(len(matrix) - 1, -1, - 1):
            matrix[i][index] = value
            value += 1
    return matrix


def snake_matrix(row, col):
    value = 1
    flag = True
    res = [[0 for i in range(col)] for j in range(row)]
    for c in range(col - 1, -1, -1):
        res = fill_col(res, c, value, flag)
        flag = not flag
        value += row
    return res


# Ex.7
def murble_puzzle(size):
    game = ["O", "X"] * size + [" "]
    target = ["O"] * size + [" "] + ["X"] * size
    i = 2 * size
    while game != target:
        if i > 0 and game[i - 1] == 'X':
            print(game, "SR")
            game = shift(game, "L")
            i -= 1
        while i > 1 and game[i - 2] == 'X':
            print(game, "JR")
            game = jump(game, "L")
            i -= 2
        if i < 2 * size and game[i + 1] == 'O':
            print(game, "SL")
            game = shift(game, "R")
            i += 1
        while i < 2 * size - 1 and game[i + 2] == 'O':
            print(game, "JL")
            game = jump(game, "R")
            i += 2

    return game


def shift(game, direction):
    if direction == "R":
        blank = game.index(" ")
        game[blank], game[blank + 1] = game[blank + 1], game[blank]
    else:
        blank = game.index(" ")
        game[blank], game[blank - 1] = game[blank - 1], game[blank]
    return game


def jump(game, direction):
    if direction == "R":
        blank = game.index(" ")
        game[blank], game[blank + 2] = game[blank + 2], game[blank]
    else:
        blank = game.index(" ")
        game[blank], game[blank - 2] = game[blank - 2], game[blank]
    return game


# Ex.19
def sum_digits(num1, num2):
    return run_sum_digits(num1) == run_sum_digits(num2)


def run_sum_digits(num):
    if num == 0:
        return 0
    return num % 10 + run_sum_digits(num // 10)


# Ex. 20
def series(n):
    if n <= 3:
        return n
    if n % 2 == 0:
        return series(n - 1) + series(n - 2) + series(n - 3)
    return abs(series(n - 1) - series(n - 3))


# Ex. 22
def ruler(n):
    if n == 0:
        return ""
    else:
        new_ruler = ruler(n - 1)
        return new_ruler + "-" * n + "\n" + new_ruler


def menu():
    choice = input("what question would you like to solve? to exit type EXIT: ")
    while choice != "EXIT":
        if choice == "13":
            lst = []
            digit = input("enter number, to stop type STOP: ")
            while digit != "STOP":
                lst.append(int(digit))
                digit = input("enter number, to stop type STOP: ")
            print(col_of_stars(lst))
        elif choice == "14":
            num1 = []
            num2 = []
            digit = input("enter digit to add to first number, to stop type STOP: ")
            while digit != "STOP":
                num1.append(int(digit))
                digit = input("enter digit to add to first number, to stop type STOP: ")
            digit = input("enter digit to add to second number, to stop type STOP: ")
            while digit != "STOP":
                num2.append(int(digit))
                digit = input("enter digit to add to first number, to stop type STOP: ")
            print(add(num1, num2))
        elif choice == "16":
            num = int(input("Enter number: "))
            print(f"with strings: {is_kaprekar_with_strings(num)}\nwithout strings: {is_kaprekar_without_strings(num)}")
        elif choice == "3":
            row = int(input("Enter number of rows in the matrix: "))
            col = int(input("Enter number of columns in the matrix: "))
            print(snake_matrix(row, col))
        elif choice == "7":
            size = int(input("Enter game size: "))
            print(murble_puzzle(size))
        elif choice == "19":
            num1 = int(input("enter first number: "))
            num2 = int(input("enter second number: "))
            print(sum_digits(num1, num2))
        elif choice == "20":
            index = int(input("enter the index of the number in the series: "))
            print(series(index))
        elif choice == "22":
            size = int(input("enter rule size: "))
            print(ruler(size))
        elif choice == "6":
            XOGame.start_playing()
        else:
            print("Invalid input, try again")
        choice = input("what question would you like to solve? to exit type EXIT: ")


menu()
