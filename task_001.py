"""Check if list has nested list and are list type"""

def is_nested(foo: list) -> bool:
    if len(foo) == 0:
        return False
    if len(foo) != 0:
        for item in foo:
            if isinstance(item, list):
                continue
            return False
    return True


def is_nested_2(foo: list) -> bool:
    if len(foo) == 0:
        return False
    return all(isinstance(item, list) for item in foo)


def is_nested_3(foo: list) -> bool:
    if len(foo) == 0:
        return False
    while True:
        for item in foo:
            if not isinstance(item, list):
                return False
        break
    return True


def is_nested_4(array):
    if len(array) == 0:
        return False
    flag = False
    for row in array:
        flag = isinstance(row, list)
        if flag is False:
            return flag
    return flag
