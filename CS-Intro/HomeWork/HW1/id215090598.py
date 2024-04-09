# Chapter 1
# Ex. 3

# price = float(input("enter the furniture price: "))
# weight = float(input("enter the furniture weight: "))
# floor = int(input("enter your floor number: "))
# distance = float(input("enter your distance from the shop: "))
# tip = price * 0.1
# transport = floor * weight + 5 * distance
# final_price = transport + tip + price
# print(f"the final price is: {final_price} ILS")

# Chapter 3
# Ex. 6

# pulse = int(input("enter your pulse while resting: "))
# weeks = int(input("how many weeks have your already trained? "))
# if 1 <= weeks <= 2 or pulse > 70:
#     print("you should run 3 km")
# elif pulse <= 70 and 3 <= weeks <= 4:
#     print("you should run 5 km")
# elif weeks >= 5:
#     if 60 <= pulse <= 70:
#         print("you should run 8 km")
#     elif pulse < 60:
#         print("you should run 10 km")

# Ex. 7

# test_grade = int(input("enter your test grade: "))
# homework_avg = int(input("enter your homework average: "))
# homework_count = int(input("how many assignments did you submit? "))
# final_grade = test_grade  # sets the final grade as the test grade, a lot of time the homework average won't count
#
# if homework_count <= 4:
#     final_grade = 0
# elif homework_count <= 6:
#     if test_grade >= 55:
#         final_grade = test_grade * 0.8 + homework_avg * 0.2
# elif homework_avg > test_grade:
#     if test_grade <= 54:
#         if homework_avg >= 80:
#             final_grade = test_grade * 0.75 + homework_avg * 0.25
#         else:
#             final_grade = test_grade * 0.8 + homework_avg * 0.2
#     else:
#         final_grade = test_grade * 0.7 + homework_avg * 0.3
#
# print(f"your final grade is {final_grade}")

# Chapter 4
# Ex. 4

# ID = int(input("enter your id: "))
# without_check_digit = ID // 10
# sum = 0
# flag = True
# for i in str(without_check_digit):
#     digit = int(i)
#     if flag:
#         sum += digit
#         flag = False
#     else:
#         multiplied = digit * 2
#         if multiplied >= 10:
#             sum += multiplied % 10 + 1
#         else:
#             sum += multiplied
#         flag = True
# check_digit = 10 - (sum % 10)
# if (check_digit == 10 and ID % 10 == 0) or (check_digit == ID % 10):
#     print("your check digit is valid")
# else:
#     print("your check digit isn't valid")

# Ex. 5

# number = input("enter number: ")
# if len(number) % 2 == 0:
#     i = 0
#     new_number = ""
# else:
#     i = 1
#     new_number = number[0]
# while i < len(number) - 1:
#     first_digit = number[i]
#     second_digit = number[i + 1]
#     new_number += second_digit + first_digit
#     i += 2
# print(new_number)

# Ex. 10

number = int(input("enter number: "))
digit = int(input("enter digit: "))
number = str(number)
divided = []
while number != "":
    divided.append(number[-digit:])
    number = number[:-digit]
divided.reverse()
new_number = ""
for num in divided:
    reversed = num[::-1]
    new_number += reversed
print(new_number)
