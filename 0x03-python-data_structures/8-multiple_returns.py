#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns a tuple with the length of a string and its first character.

    Args:
        sentence: Sentence to work with
    Return:
        Tuple
    """
    howLong = len(sentence)

    if howLong == 0:
        return (howLong, "None")
    return (howLong, sentence[0])
