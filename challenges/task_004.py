""" Create function that takes list as argument. Function should swap first and last element of the list. """

def swap_elements(array: list) -> list:
    tmp = array[0]
    array[0] = array[-1]
    array[-1] = tmp
    return array


def swap_elements_2(array: list) -> list:
    (array[0], array[-1]) = (array[-1], array[0])
    return array
