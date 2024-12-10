# Import utils file in order to get the functionality from them
from utils import play_turn

# Global variables
TARGET_SCORE = 50
FILENAME = "scores.txt"

# Introduction to game
# Prompt user to enter starting information
print('Welcome to the "Tuple Out" Dice Game!')
player1 = input("Enter the name of Player 1: ")
player2 = input("Enter the name of Player 2: ")
print(f"Thank you for playing {player1} and {player2}")
print('''You will be playing against each other and will take turns rolling 3 dice to earn points.
If all 3 dice have the same value, then you have "tupled out" and earn 0 points that round.
If only 2 of the die have the same value but not all, then those become "fixed" and cannot be rerolled.
You may reroll any die that are not fixed until you get a value you like.
Just be careful to not "tuple out" when rerolling. Happy playing!
''')
print(f"The first to score {TARGET_SCORE} points wins!")

# Dictionary holding scores of each player, intitialized to 0
scores = {player1: 0, player2: 0}

# Stores whose turn it is
# Even numbers will designate it is player1's turn, odds for player2
turn = 0  

'''
Main game loop
While loop keeps game running until one player reaches target score 
'''
while scores[player1] < TARGET_SCORE and scores[player2] < TARGET_SCORE:
	# Even is player 1, odd is player 2
	if turn % 2 == 0:
		current_player = player1
	else:
		current_player = player2
	# Simulate each players turn
	score = play_turn(current_player)
	# Add each players sore to dictionary
	scores[current_player] += score
	print(f"\nScores: {scores}")
	# Increment turn by 1 each round under a player reaches target score
	turn += 1

if (scores[player1] >= TARGET_SCORE):
	winner = player1
else:
	winner = player2
print(f"\n{winner} wins with a score of {scores[winner]}!")
with open(FILENAME, "w") as f:
	f.write("Winner was {winner} with a score of {scores[winner]}")
print("Thanks for playing!")