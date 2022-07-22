""" Write a function that takes text as argument and reverse words order. """

def reverse_words(text: str) -> str:
    split_words = reversed(text.split())
    result = " ".join(split_words)
    return result


def reverse_words_2(text: str) -> str:
    word_list = text.split()
    return " ".join(word_list[::-1])
