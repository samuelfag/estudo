# https://www.codewars.com/kata/523f5d21c841566fde000009/train/python


def array_diff(a, b):
    list_result = []
    for i in a:
        if i in b:
            pass
        else:
            list_result.append(i)
    return list_result


array_diff([], [1, 2])
