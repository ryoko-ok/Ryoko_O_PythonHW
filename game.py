# import the randompackage so that we can generate a random choice
from random import randint
from gameFunctions import winlose, gameWars, compare
from Example import compareStuff

while gameWars.player == False:
# set player to True
	print("..*..*..*..*..*..*..*..*..*..*..*..*..\n")
	print("gameWars.Computer lives; ", My life Points "\n")
	print("Player lives; ", Your life Points "\n")
	print("Choose your weapon!\n")
	print("..*..*..*..*..*..*..*..*..*..*..*..*..\n")

	player = input ("choose rock, paper or scissors: ")
	player = player.lower()

	print("gameWars.computer chose", gameWars.computer, "\n")
	print("player chose", player, "\n")

	### this is where you would call compare
	
	#### end compare stuff


	# handle all lives lost for player or AI
	if gameWars.player_lives is 0:
		winlose.winorlose("lost")
	# if player_lives is 0:
	# 	print("Out of lives! you suck at this game. Would you like to play again?\n")
	# 	choice = input ("Y / N")
	# 	print(choice)

	# 	if (choice is "N") or (choice is "n"):
	# 		print("You chose to quit.")
	# 		exit()

	# 	elif (choice is "Y") or (choice is "y"):
	# 		# reset the game so that we can start all over again
	# 		player_lives = 5
	# 		gameWars.computer_lives = 5
	# 		player = False
	# 		gameWars.computer = choices[randint(0,2)]


	elif gameWars.computer_lives is 0:
		winlose.winorlose("lost")

		# print("gameWars.Computer is out of lives! you suck at this game. Would you like to play again?\n")
		# choice = input ("Y / N")
		# print(choice)

		# if (choice is "N") or (choice is "n"):
		# 	print("You chose to quit.")
		# 	exit()

		# elif (choice is "Y") or (choice is "y"):
		# 	# reset the game so that we can start all over again
		# 	player_lives = 5
		# 	gameWars.computer_lives = 5
		# 	player = False
		# 	gameWars.computer = choices[randint(0,2)]

	else:
		# need to check all of our conditions after checking for a tie
		player = False
		gameWars.computer = gameWars.choices[randint(0, 2)]
