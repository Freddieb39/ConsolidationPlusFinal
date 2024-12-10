# Import random library to be able to simulate the rolling of dice
import random

'''
Rolls three dice and returns the result as a tuple
Uses random's randint method to generate random number between 1 and 6 three times
'''
def roll_dice():
	die_tuple = (random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))
	return die_tuple

'''
@ Parameters
die_tuple = the tuple returned from the roll_dice method holding the user's rolled die
Checks to see if all are the same value and if so, returns True, otherwise returns False
'''
def is_tupled_out(die_tuple):
	# Associative property, if a = b and b = c then a = c must be true
	# This means that they are all equal
	if die_tuple[0] == die_tuple[1] and die_tuple[0] == die_tuple[2]:
		return True
	else:
		return False
		
'''
@ Parameters
die_tuple = the tuple returned from the roll_dice method holding the user's rolled die
Checks to see if all are the same value and if so, returns True, otherwise returns False
'''
def get_fixed(die_tuple):
	fixed = [False, False, False]
	for i in range(len(die_tuple)):
		for j in range(len(die_tuple)):
			# If you are not looking at the same die and two different die have the same value, they are "fixed"
			if i != j and die_tuple[i] == die_tuple[j]:
				fixed[i] = True
				fixed[j] = True
	return fixed

'''
@ Parameters
die_tuple = the tuple returned from the roll_dice method holding the user's rolled die
Return sum of all dice in the tuple
'''
def calculate_points(die_tuple):
	sum = 0	
	# Adds all values to sum
	for i in range(len(die_tuple)):
		sum += die_tuple[i]
	return sum
	
'''
@ Parameters
die_tuple = the tuple returned from the roll_dice method holding the user's rolled die
fixed = an array of boolean values determining if each index in tuple should fixed or if it's available to be rerolled
Return a new tuple of the dice after being rerolled
'''
def reroll_dice(die_tuple, fixed):
	rerolled_die_tuple = [die_tuple[0], die_tuple[1], die_tuple[2]]
	# Loop through die_tuple and if there are any that are not fixed, they are eligible to be rerolled
	for i in range(len(die_tuple)):
		if not fixed[i]:
			rerolled_die_tuple[i] = random.randint(1, 6)
	return tuple(rerolled_die_tuple)
'''
@ Parameters
player_name = the String of the player's name so the method know's who is up currently
Simulates a single turn for a player
Roll a dice, if they "tuple out", their turn ends with 0 points
If there are any fixed, they get a chance to reroll non-fixed dice
When they are satisfied, they can stop their turn
'''
def play_turn(player_name):
	print(f"\n{player_name}'s turn!")
	dice = roll_dice()
	print(f"Rolled: {dice}")
    
	# Keep track of players turn
	turn_ended = False
	# Keep track of fixed dice using an array
	fixed = [False, False, False]
	# Players points for the turn
	points = 0
	while not turn_ended:
        # Check if player has "tupled out"
		if is_tupled_out(dice):
			print("Tupled out! No points this turn.")
			points = 0
			turn_ended = True
		else:
			# Get which dice are fixed
			fixed = get_fixed(dice) 
			# If none are fixed print the calculated points the user would get
			player_points = calculate_points(dice)    
			print(f"This would be {player_points} points")
			points = player_points
			# Prompt user to reroll if they want to
			decision = input("Do you want to reroll unfixed dice? (y/n): ")
			# If not rerolling, end the turn and calculate their total points
			if decision.lower() == 'n':
				player_points = calculate_points(dice)
				print(f"Turn ended: You earn {player_points} points.")
				points = player_points
				turn_ended = True
			# If they are rerolling, call the reroll method and restart while loop with new dice
			else:
		        # Reroll unfixed dice
				dice = reroll_dice(dice, fixed)
				print(f"Rolled: {dice}")
	# Return the users points for that round
	return points