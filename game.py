#import the randompackage so that we can generate a random choice
from random import randint

#choices is an array =>a arrray is a container that can hold multiple values
choices= ["rock", "paper", "scissors"]

#set the computer variable to one of these choices
computer = choices[randint(0, 2)]

#set up the game loop so that we don't have to restart all the time
player = False

while player is False:
#set player to True
	print("*****************************\n\n")
	print("Choose your weapon!\n\n")
	print("*****************************\n\n")

	player = input("choose rock, paper or scissors: ")

	print("computer chose ", computer, "\n")
	print("player chose ", player, "\n")

	if player == "quit":
		exit()
	elif computer == player:
		print("tie! no one wins, play again")
	elif player == "Rock":
		if computer == "Paper":
			print("You lose!", computer, "covers", player, "\n")
		else:
			prnt("You win!", player, "smashes through", computer, "\n")

	elif player == "Paper":
		if computer == "Scissors":
			print("You lose!", computer, "cuts", player, "\n")
		else:
			prnt("You win!", player, "smashes", computer, "\n")

	elif player == "Scissors":
		if computer == "Rock":
			print("You lose!", computer, "smashes", player, "\n")
		else:
			prnt("You win!", player, "cuts", computer, "\n")

	else:
		print("That's not a valid choice, try again")

# need to check all of our conditions after checking for a tie
		player = False
		computer = choices[randint(0, 2)]
