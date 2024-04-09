def stars(num):
    if num <= 0:
        return
    print("*")
    stars(num - 1)


def triangle(num):
    if num <= 0:
        return
    triangle(num - 1)
    print("*" * num)


def fact(num):
    if num <= 0:
        return 1
    return num * fact(num - 1)


def power(n, k):
    if k == 0:
        return 1
    temp = power(n, k // 2)
    back = temp * temp
    if k % 2 == 0:
        return back
    return n * back


