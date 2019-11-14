from gameFunctions import gameWars

# what are you trying to compare inside this function?
# you will need to pass those things in as arguments
# inside the round brackets
def comparechoices():
	if player.lower() == "quit":
		exit()

	elif gameWars.computer == player:
		print("tie! no one wins, play again")

	elif player.lower() == "rock":
		if gameWars.computer == "paper":
			print("You lose!", gameWars.computer, "covers", player, "\n")
			gameWars.player_lives = player_lives - 1
		else:
			print("You win!", player, "smashes through", gameWars.computer, "\n")
			gameWars.computer_lives = gameWars.computer_lives - 1

	elif player.lower() == "paper":
		if gameWars.computer == "scissors":
			print("You lose!", gameWars.computer, "cuts", player, "\n")
			player_lives = player_lives - 1
		else:
			print("You win!", player, "covers", gameWars.computer, "\n")
			gameWars.computer_lives = gameWars.computer_lives - 1

	elif player.lower() == "scissors":
		if gameWars.computer == "rock":
			print("You lose!", gameWars.computer, "smashes", player, "\n")
			player_lives = player_lives - 1
		else:
			print("You win!", player, "cuts", gameWars.computer, "\n")
			gameWars.computer_lives = gameWars.computer_lives - 1

	else:
		print("That's not a valid choice, try again")
