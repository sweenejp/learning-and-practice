attendees = ['Ken', 'Alena', 'Treasure']
attendees.append('Joe')
others = ['Jake', 'Bill']
optional_attendees = ["Flair", "Jason"]
attendees.extend(others)
print(attendees)

# .join takes a list and joins it with whatever is in the quotes
to_line = "PPPPPP ".join(attendees)
cc_line = ", ".join(optional_attendees)
print("To: " + to_line)
print("Cc: " + cc_line)

# .split converts a string to a list. The parameter is what will seperate each item.
buttheads = cc_line.split(", ")
print(buttheads[0] + " is a total butthead")



