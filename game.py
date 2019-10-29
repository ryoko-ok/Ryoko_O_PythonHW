#import the randompackage so that we can generate a random choice
from random import randint

#choices is an array =>a arrray is a container that can hold multiple values
choices = ["rock", "paper", "scissors"]

#set the computer variable to one of these choices
computer = choices[randint(0, 2)]

#set up the game loop so that we don't have to restart all the time
player = False

while player == False:
#set player to True

	print("*****************************\n\n")
	print("Choose your weapon!\n\n")
	print("*****************************\n\n")

	player = input("choose rock, paper or scissors: ")

	print("computer chose ", computer, "\n")
	print("player chose ", player, "\n")

	if player.lower() == "quit":
		exit()
	elif computer == player:
		print("tie! no one wins, play again")
	elif player.lower() == "rock":
		if computer == "paper":
			print("You lose!", computer, "covers", player, "\n")
		else:
			print("You win!", player, "smashes through", computer, "\n")

	elif player.lower() == "paper":
		if computer == "scissors":
			print("You lose!", computer, "cuts", player, "\n")
		else:
			print("You win!", player, "covers", computer, "\n")

	elif player.lower() == "scissors":
		if computer == "rock":
			print("You lose!", computer, "smashes", player, "\n")
		else:
			print("You win!", player, "cuts", computer, "\n")

	else:
		print("That's not a valid choice, try again")

# need to check all of our conditions after checking for a tie
	player = False
	computer = choices[randint(0, 2)]
