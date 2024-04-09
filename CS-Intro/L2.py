# 1
first_number = int(input("enter first number: "))
second_number = int(input("enter second number: "))
third_number = int(input("enter third number: "))
string = input("enter string: ")
print((string + first_number / second_number + string) * third_number)  # supposed to be an error-
# can't add float to string

# 2
time = int(input("enter the time: "))
hour = time // 100
minute = time % 100
print(f"{hour}:{minute}")

# 3
number = int(input("enter number: "))
left_pair = number // 100
right_pair = number % 100
left_sum = left_pair // 10 + left_pair % 10
right_sum = right_pair // 10 + right_pair % 10
print(right_sum == left_sum // 2)
