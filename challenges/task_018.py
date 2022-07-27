""" Define a function that takes for arguments string sequence and returns list with all possible permutations
of the sequence. """

from itertools import permutations

def calculate(sentence: str) -> list:
    words = sentence.split()
    permuted = list(permutations(words))
    result = [" ".join(item) for item in permuted]
    return result
