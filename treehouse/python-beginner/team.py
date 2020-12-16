# TODO Create an empty list to maintain the player names
player_names = []

# TODO Ask the user if they'd like to add players to the list.
wants_to_add = input("Would you like to add a player to the team?\nYes/no:  ")

# If the user answers "Yes", let them type in a name and add it to the list.
while wants_to_add.lower() == "yes":
    new_player = input("Enter the name of the player: ")
    player_names.append(new_player)
    wants_to_add = input("Would you like to add a player to the team?\nYes/no:  ")

# If the user answers "No", print out the team 'roster'
# TODO print the number of players on the team

print("\nThere are {} players on your team.".format(len(player_names)))

# TODO Print the player number and the player name
# The player number should start at the number one

player_number = 1
for player in player_names:
    print("Player {}: {}".format(player_number, player))
    player_number += 1

# TODO Select a goalkeeper from the above roster

keeper = input("Please select the goalkeeper by entering that person's player number. (1-{}): ".format(len(player_names)))

keeper = int(keeper)

print("Great!!! The goalkeeper for the game will be {}.".format(player_names[keeper - 1]))


# TODO Print the goal keeper's name
# Remember that lists use a zero based index