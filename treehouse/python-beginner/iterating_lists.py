rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

for index, item in enumerate(rainbow, 1):
    print(f'{index}. {item}')


for item in enumerate(rainbow, 0):
    print(item[0])
    print(item[1])