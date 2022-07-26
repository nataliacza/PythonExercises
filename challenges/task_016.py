""" Write a function that takes list with numbers and removes all numbers that has repeated numbers in it,
ex. [122, 34, 51] -> [34, 51]. """

def remove_repetitive(array: list) -> list:
    duplicates = list()
    for value in array:
        if value < 10:
            continue
        tmp = list(str(value))
        if not len(tmp) == len(set(tmp)):
            duplicates.append(value)

    for element in duplicates:
        if element in array:
            array.remove(element)

    return array


def remove_repetitive_2(array: list) -> list:
    result = list()
    for num in array:
        if len(set(str(num))) == len(str(num)):
            result.append(num)
    # result = [num for num in array if len(set(str(num))) == len(str(num))]
    return result
