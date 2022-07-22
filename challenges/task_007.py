""" Write a function that takes 2 lists as arguments, removes its common elements and returns both lists. """

def remove_common_elements(array1: list, array2: list) -> tuple:
    for elem in array1[:]:
        if elem in array2:
            array1.remove(elem)
            array2.remove(elem)
    return array1, array2
