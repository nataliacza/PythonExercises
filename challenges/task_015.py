""" Write a function that takes nested list with dictionaries and leaves only dicts with key="level". """

def filter_users(array: list) -> list:
    for index, dictionary in enumerate(array):
        if not dictionary.get("level"):
            del array[index]
    return array

def filter_users_2(array: list) -> list:
    return list(filter(lambda user: "level" in user.keys(), array))

def filter_users_3(array: list) -> list:
    return [user for user in array if "level" in user.keys()]
