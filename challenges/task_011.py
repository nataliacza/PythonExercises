""" Create function that takes for argument two nested lists and returns one list where each nested list remains on
the same index in result, ex. [[1, 1], [2, 2]] + [[3, 3], [4, 4]] = [[1, 1, 3, 3], [2, 2, 4 , 4]]. """

# Using zip()
def concat(array1: list, array2: list) -> list:
    zipped = list(zip(array1, array2))
    result = list()
    for pair in zipped:
        tmp = pair[0]
        tmp.extend(pair[1])
        result.append(tmp)
    return result

# Using enumerate()
def concat_2(array1: list, array2: list) -> list:
    result = list()
    for index, value in enumerate(array1):
        result.append(value)
        result[index].extend(array2[index])
    return result

# Nested element in array1 extended by array2
def concat_3(array1: list, array2: list) -> list:
    for index, value in enumerate(array1):
        array1[index].extend(array2[index])
    return array1
