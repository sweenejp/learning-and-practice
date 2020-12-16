shopping = []


def add_to_list(item):
    shopping.append(item)
    if len(shopping) < 2:
        print("{} was added to your shopping list. There is 1 item in your shopping list".format(item))
    else:
        print("{} was added to your shopping list. There are {} items in your shopping list".format(item, len(shopping)))


def show_help():
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your list.
""")


def show_list(any_list):
    print("Here is your shopping list: ")
    list_string = ", ".join(any_list)
    print(list_string)


# also could have done:
# def show_list():
#     print("Here is your shopping list: ")
#     for item in shopping:
#         print(item)


show_help()


while True:
    new_item = input("> ")
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list(shopping)
        continue
    add_to_list(new_item)
show_list(shopping)
