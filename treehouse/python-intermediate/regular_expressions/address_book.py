import re


def phone_numbers(string):
    return re.findall(r'\d{3}-\d{3}-\d{4}', string)


def find_words(count, string):
    return re.findall(r'\w' * count + r'\w*', string)


def find_emails(string):
    return re.findall(r'[-\w\d+.]+@[-\w\d.]+', string)


names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()

# first_name = r'Kenneth'
# last_name = r'Love'
# # print(re.match(last_name, data))
# # print(re.search(first_name, data))
# #
# # print(re.findall(r'\w*, \w+', data))
#
# # print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-?\s?\d{4}', data))
# print(phone_numbers(data))
# print(find_words(4, "dog, cat, baby, balloon, me"))
# print(re.findall(r'\b[trehous]{9}\b', data, re.I))

# print(re.findall(r'''
#     \b@[-\w\d.]* # first a word boundary, an @, and then any number of characters
#     [^gov\t]+ # ignore one or more instances of the letters 'g', 'o', 'v', or a tab
#     \b # match another word boundary
# ''', data, re.VERBOSE | re.I))
#
# print(re.findall(r"""
#     \b[-\w]+, # find a word boundary, 1+ hyphens or characters, and a comma
#     \s # find 1 whitespace
#     [-\w ]+ # 1+ hyphen and characters and explicit spaces
#     [^\t\n] # ignore tabs and newlines
# """, data, re.X))

line = re.compile(r'''
    ^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t # last and first names
    (?P<email>[-\w\d+.]+@[-\w\d.]+)\t # email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t # phone
    (?P<job>[-\w ]+,\s[-\w. ]+)\t? # job and company
    (?P<twitter>@[\w\d]+)$ # twitter
''', re.X | re.MULTILINE)

for match in line.finditer(data):
    print('{first} {last} <{email}>'.format(**match.groupdict()))




