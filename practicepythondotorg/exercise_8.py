# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner, and ask if the players want
# to start a new game)

print("Type 'quit' at any point to exit.")

while True:
    player1 = input("Player 1. Choose rock, paper, or scissors: ").lower()
    if player1 == "quit":
        break
    else:
        player2 = input("Player 2. Choose rock, paper, or scissors: ").lower()
        if player2 == "quit":
            break
        elif player1 == player2:
            print("Draw!")
        elif player1 == "rock":
            if player2 == "paper":
                print("Player 2 wins!")
            else:
                print("Player 1 wins")
        elif player1 == "paper":
            if player2 == "scissors":
                print("Player 2 wins!")
            else:
                print("Player 1 wins!")
        elif player1 == "scissors":
            if player2 == "rock":
                print("Player 2 wins!")
            else:
                print("Player 1 wins!")

# while True:
#     usr_command = input("Enter your command: ")
#     if usr_command == "quit":
#         break
#     else:
#         print("You typed " + usr_command)
