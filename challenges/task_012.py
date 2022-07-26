""" Create function that takes for argument two nested list and returns new list, which joins elements in nested list
on the same index, ex. [[1], [3]] + [[2], [4]] = [[1, 2], [3, 4]]. Check if there are the same amount of nested list,
if not raise ValueError. """


def concat(array1: list, array2: list) -> list:
    if not len(array1) == len(array2):
        raise ValueError("The given lists are not of the same length.")
    result = list()
    for index, value in enumerate(array1):
        result.append(array1[index])
        result[index].extend(array2[index])
    return result
