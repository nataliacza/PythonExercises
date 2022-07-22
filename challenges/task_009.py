""" Create function that takes list as argument and returns list of indexes with str value. """

def get_indices(array: list) -> list:
    result = [index for index, value in enumerate(array) if isinstance(value, str)]
    return result
