""" Check if you can build matrix. Given array must contain lists and each nested list must have the same amount
of elements. You can use functions is_nested() and is_all_equal(). """

def is_nested(array):
    if len(array) == 0:
        return False
    return all(isinstance(row, list) for row in array)

def is_all_equal(iterator):
    return len(set(iterator)) <= 1

def is_valid_array(foo: list) -> bool:
    if is_nested(foo):
        number_of_elements = len(foo[0])
        for array in foo:
            if len(array) != number_of_elements:
                return False
            else:
                continue
        return True
    return False

def is_valid_array_2(array):
    if is_nested(array):
        if is_all_equal(len(row) for row in array):
            return True
    return False
