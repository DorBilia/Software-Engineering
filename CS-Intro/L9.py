def sum_mat(matrix):
    sum = 0
    for row in matrix:
        for i in row:
            sum += i
    return sum


def sum_diag(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][len(matrix) - i - 1]
    return sum


def sum_col(matrix):
    for i in range(len(matrix[0])):
        sum = 0
        for j in range(len(matrix)):
            sum += matrix[j][i]
        print(sum)


def char_in_list(size):
    arr = []
    for i in range(size):
        item = input("enter character")
        arr.append(item)
    char = input("enter character to search")
    count = 0
    for i in arr:
        if i == char:
            count += 1
    print(count)
    return arr


def char_in_two_lists(size):
    arr1 = []
    for i in range(size):
        item = input("enter character to 1 ")
        arr1.append(item)
    arr2 = []
    for i in range(size):
        item = input("enter character to 2")
        arr2.append(item)
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                print(i, j)




mat = [[1, 2, 3], [2, 4, 6], [5, 5, 5]]
