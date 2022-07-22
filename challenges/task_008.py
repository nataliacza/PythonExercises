""" Create function that takes for argument: list and searchable value. Function returns indexes of elements found. """

def get_indices(array: list, searched) -> list:
    found_indexes = []
    for i in range(len(array)):
        if array[i] == searched:
            found_indexes.append(i)
    return found_indexes


def get_indices_2(array: list, searched) -> list:
    found_indexes = [i for i in range(len(array)) if array[i] == searched]
    return found_indexes


def get_indices_3(array: list, searched) -> list:
    found_indexes = [index for index, value in enumerate(array) if value == searched]
    return found_indexes
