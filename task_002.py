"""Check if list elements are all the same."""

def is_all_equal(foo: list) -> bool:
    x = foo[0]
    for item in foo:
        if item != x:
            return False
    return True

def is_all_equal_2(foo: list) -> bool:
    return len(set(foo)) <= 1
