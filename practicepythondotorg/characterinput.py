name = input("What is your name? ")
age = int(input("What is your age? "))
magic_number = int(input("What is your magic number? "))
current_year = 2020
y_hundred = 100 - age + current_year
message = "Hello {}! You will turn 100 years old in the year {}\n".format(name, y_hundred)

print(message * magic_number)