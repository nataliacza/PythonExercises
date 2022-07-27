""" Define a function that takes for arguments list and integer k. Function should return all elements from the list,
 that are k away from value. Skip first and last element of the list in result. """

def calculate(array: list, k: int = 5) -> list:
    result = []
    for index in range(1, len(array) - 1):
        if abs(array[index - 1] - array[index]) >= k \
                and abs(array[index + 1] - array[index]) >= k:
            result.append(array[index])
    return result
