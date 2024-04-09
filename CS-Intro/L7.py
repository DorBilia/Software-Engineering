def list_from_num(number):
    i = 0
    list = [number % 10]
    number //= 10
    while number != 0:
        list.append(number % 10)
        number //= 10
        i += 1
    return list


def sum_of_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum


def sum_numbers():
    sum = 0
    num = int(input("Enter a number: "))
    flag = True
    list = list_from_num(num)
    while flag:
        if len(list) == 3 and list[0] == list[1] == list[2]:
            flag = False
        else:
            sum += num
            num = int(input("Enter another number: "))
            list = list_from_num(num)
    return sum


# sum = sum_numbers()
# sum_list = list_from_num(sum)
# print(sum_of_list(sum_list))

def dig_in_number(num, dig):
    count = 0
    while num != 0:
        if num % 10 == dig:
            count += 1
        num //= 10
    return count


def every_dig_in_number(num):
    list_counts = []
    res = ""
    for i in range(0, 10):
        list_counts.append(dig_in_number(num, i))
    for i in range(0, len(list_counts)):
        res += f"{i}: {list_counts[i]}\n"
    return res

# print(every_dig_in_number(123450055))
