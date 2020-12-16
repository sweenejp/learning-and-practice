import re

string = 'Perotto, Pier Giorgio'

names = re.match(r"([\w]*), ([\w]*\s[\w]*)", string)

print(names)