def is_valid_email(email):
    if email.count("@") == 1:
        if 8 <= len(email) <= 30:
            user = email[:email.index("@")]
            if check_is_has_lower_or_upper(user):
                server = email[email.index("@"):]
                if "." in server:
                    if server[-1].isalpha() and server[-2].isalpha():
                        return True
    return False


def check_is_has_lower_or_upper(string):
    if not string[0].isalpha():
        return False
    if string.isupper() or string.islower():  # isupper and islower check only strings and ignore numbers
        return False
    return True


def run_max_couple(numbers, i, j):
    if i > j:
        return numbers[i] + numbers[j]
    if i == j:
        return numbers[i]
    sum = numbers[i] + numbers[j]
    if sum > run_max_couple(numbers, i + 1, j - 1):
        return sum
    return run_max_couple(numbers, i + 1, j - 1)


def max_couple(numbers):
    if numbers:
        max = run_max_couple(numbers, 0, len(numbers) - 1)
        return f"Max couple in {numbers} is {max}"
    return "List is empty"


def has_square_with_sum(matrix, num):
    for i in range(len(matrix) - 2):
        for j in range(len(matrix[0]) - 2):
            if matrix[i][j] + matrix[i][j + 1] + matrix[i + 1][j] + matrix[i + 1][j + 1] == num:
                return f"{i},{j}"
    return "-1,-1"


# print(has_square_with_sum([[5, 8, 3, 0, 9], [2, 1, 2, 7, 4], [3, 4, 2, 8, 2], [7, 7, 6, 2, 8]],10))
def find_sequence_number(matrix, num):
   pass