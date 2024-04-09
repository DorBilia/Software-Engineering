# into
# 1
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# result = 1
# for i in range(num2):
#     result *= num1
# print(result)

# 2
# num = input("Enter a number: ")
# while num[0] != num[1] != num[2]:
#     num = input("Enter a number: ")
# print(int(num[0]) + int(num[1]) + int(num[2]))

#  functions
def bigger(num1, num2):
    if num1 > num2:
        return num1
    return num2


# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print(f"the max is: {bigger(num1, num2)}")

def multiply(num):
    sum = 1
    for i in range(1, num + 1):
        sum *= i
    return sum


def choose(n, k):
    return multiply(n) / (multiply(k) * multiply(n - k))


def digit_in_number(num, digit):
    count = 0
    while num != 0:
        if num % 10 == digit:
            count += 1
        num //= 10
    return count
