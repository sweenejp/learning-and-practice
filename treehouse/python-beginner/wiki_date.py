import datetime


answer_format = '%m/%d'
# Wikipedia links to dates in this format:
link_format = '%b_%d'
link = 'https://en.wikipedia.org/wiki/{}'

while True:
    answer = input("What date would you like? Please use the MM/DD format. Enter 'quit to quit. ")
    if answer.upper() == 'QUIT':
        break

    try:
        # convert the user input to a datetime
        date = datetime.datetime.strptime(answer, answer_format)
        # convert the datetime back into a string with wikipedia's format
        output = link.format(date.strftime(link_format))
        print(output)
    except ValueError:
        print("Please use the format MM/DD")
