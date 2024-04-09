# 1 checks if two 3-digit-numbers have the same digits
# number1 = int(input("enter first 3 digit number: "))
# number2 = int(input("enter second 3 digit number: "))
# first1 = number1 % 10
# second1 = (number1 // 10) % 1010
# third1 = number1 // 100
# first2 = number2 % 10
# second2 = (number2 // 10) % 10
# third2 = number2 // 100
# flag = False
# if first1 == first2 or first1 == second2 or first1 == third2:
#     if second1 == second2 or second1 == third2 or second1 == first2:
#         if third1 == third2 or third1 == first2 or third1 == second2:
#             if first2 == first1 or first2 == second1 or first2 == third1:
#                 if second2 == second1 or second2 == third1 or second2 == first1:
#                     if third2 == third1 or third2 == first1 or third2 == second1:
#                         flag = True
# print(flag)

# 2 checks if 42 is in a list
# num1 = int(input("enter number: "))
# num2 = int(input("enter number: "))
# num3 = int(input("enter number: "))
# arr = [num1, num2, num3]
# print(42 in arr)

# 4
num = int(input("enter number: "))
sum = num
while sum != 42:
    print(sum)
    num = int(input("enter number: "))
    sum += num
print(sum)
