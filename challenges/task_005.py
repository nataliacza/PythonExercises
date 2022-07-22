""" Create function that takes for arguments: list, index, index. Swap two index and return list. """

def swap_elements(array: list, index_one: int, index_two: int) -> list:
    (array[index_one], array[index_two]) = (array[index_two], array[index_one])
    return array


def swap_elements_2(array: list, index_one: int, index_two: int) -> list:
    tmp = array[index_one]
    array[index_one] = array[index_two]
    array[index_two] = tmp
    return array
