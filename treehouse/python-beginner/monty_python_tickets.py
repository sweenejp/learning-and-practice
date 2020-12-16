SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100

def calculate_price(number_of_tickets):
    # $2 service charge per transaction
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining > 0:

    print("There are only {} tickets remaining!\nBuy now to secure your spot for the show!".format(tickets_remaining))
    name = input("Hi there! What's your name? ")
    order = input("Okay, {}, how many tickets would you like? ".format(name))
    try:
        order = int(order)
        if order > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        # Include the error text in the output
        print("Oh no, we ran into an issue.")
        print("{} Please try again".format(err))
    else:
        amount_due = calculate_price(order)
        print("Great, {}! You ordered {} tickets. Your amount due is ${}".format(name, order, amount_due))
        intent_to_purchase = input('Do you want to proceed with your purchasing order?\nPlease enter "yes" or "no" ')
        if intent_to_purchase.lower() == 'yes':
            print('SOLD!')
            tickets_remaining -= order
        else:
            print('Thank you for stopping by, {}.'.format(name))
print('We are so sorry! This event is sold out. :(')

