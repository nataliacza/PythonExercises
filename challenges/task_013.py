""" Define a function that takes for argument nested list and sort elements ascending by each nested list. """

def sort_by_row(array: list) -> list:
    for index, value in enumerate(array):
        array[index] = sorted(array[index])
    return array

def sort_by_row_2(array: list) -> list:
    for item in array:
        item.sort()
    return array
