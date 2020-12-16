import re


def find_words(count, string):
    return re.findall(r"\w{count}", string)
