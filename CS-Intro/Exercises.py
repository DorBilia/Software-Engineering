# Ex.1

# age = int(input("enter your age: "))
# if age < 18:
#     print("you are an amateur")
# elif age < 65:
#     print("you are an adult")
# else:
#     print("you are retired")

# Ex.2

# number = int(input("enter a 3 digit number: "))
# first_dig = number % 10
# second_dig = (number // 10) % 10
# third_dig = number // 100
# print(first_dig == second_dig == third_dig)

# Ex.2-string

# number = input("enter a 3 digit number: ")
# first_dig = number[2]
# second_dig = number[1]
# third_dig = number[0]
# print(first_dig == second_dig == third_dig)

# Ex.3

# number = int(input("enter a 3 digit number: "))
# first_dig = number % 10
# second_dig = (number // 10) % 10
# third_dig = number // 100
# if first_dig == second_dig + 1 and third_dig + 1 == second_dig:
#     print(True)
# else:
#     print(False)

# Ex.4
#
# number1 = int(input("enter first number: "))
# number2 = int(input("enter second number: "))
# number3 = int(input("enter third number: "))
# if number1 + number2 >= number3 or number3 + number2 >= number1 or number3 + number1 >= number2:
#     print("the numbers are ribs of a triangle")
# else:
#     print("the numbers are not ribs of a triangle")

# Ex.5

# num = int(input("enter number: "))
# digit = int(input("enter digit: "))
# print(num * 10 + digit)

# Ex. 6

# age = int(input("enter your age: "))
# weight = int(input("enter your weight: "))
# height = int(input("enter your height: "))
# difference = height / weight
# message = "no diet available"
# if 0.5 <= difference < 2 and 11 < age < 40:
#     message = "diet A"
# elif 2 <= difference < 3.5:
#     if 11 < age < 20:
#         message = "diet B"
#     elif 21 < age < 40:
#         message = "diet C"
# print(message)

# Ex. 7

# numbers = [3, 9, 42]
# if 42 in numbers:
#     print("42 in list")
# else:
#     print("42 not in list")
# print(len(numbers), numbers[2])
# string = input("enter a string: ")
# if "K" in string:
#     print("K in string")
# else:
#     print("K not in string")
# print(string[2])
