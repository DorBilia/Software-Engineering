def run_list_42(list, size):
    if size >= len(list) or len(list) == 0:
        return 0
    if list[size] == 42:
        return run_list_42(list, size + 1) + 1
    else:
        return run_list_42(list, size + 1)


def list_42(list):
    return run_list_42(list, 0)


def run_max(list, size):
    if size == 0:
        return 0
    if list[size - 1] >= run_max(list, size - 1):
        return list[size - 1]
    return run_max(list, size - 1)


def max_in_list(list):
    return run_max(list, len(list))


list = [1, 42, 3, 45, 42, 6]
print(max_in_list(list))
