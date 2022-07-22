""" Create function that takes as argument list of dictionaries [{a:b, c:d}, {a:b, c:d}...] and returns dictionary with
 grouped by key elements. """

def convert(array: list) -> dict:
    result = {}
    for item in array:
        for key, value in item.items():
            if key not in result:
                result[key] = [value]
            else:
                result.get(key).append(value)
    return result
