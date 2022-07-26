""" Define a function that takes for argument nested list and returns top 3 elements from each list sorted descending.
Each nested list has at least 3 elements. """

def top3(array: list) -> list:
    result = list()
    for item in array:
        result.append(sorted(item, reverse=True)[:3])
    return result

def top3_2(array: list) -> list:
    for index, value in enumerate(array):
        value.sort(reverse=True)
        array[index] = value[:3]
    return array
