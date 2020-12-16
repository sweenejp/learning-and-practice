import re


def first_number(string):
    return re.search(r'\d', string)


def numbers(count, string):
    return re.search((r'\d' * count), string)