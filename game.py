import random
import math

x=0
y=0

bad = [(17,7),(54,34),(64,60),(62,19),(87,24),(93,73),(95,75),(99,78),
	# Ladder points
	(4,14),(9,31),(20,38),(28,84),(40,59),(51,67),(63,81),(71,91)]
59
player = [0,0]

def game(player):
	no =0
	while no != 100:
		print("\n\n--------------************--------------------\n")
		input("Press Enter For Next Move")

		x=player[0]
		y=player[1]

		no = x*10+y
	
		dice = throw_dice()
		print("Dice Gives ",dice)


		if no + dice > 100 :
			print("Roll Again")
			continue

			

		y=y+dice

		if y>10 :
			y=y-10
			x=x+1

		if player == (10,10):
			print("Limit Reached")
			break

		player[0] = x
		player[1] = y
		player = check_pos(player)


	print("\nGame Ended")

def throw_dice():
	return random.randint(1,6)

def check_pos(player):
	temp = player[0]*10+player[1]
	print("player",temp)
	# player_pos = 
	for check in bad:
		if temp == check[0]:
			print("\n\n\t\t==================================\n\n")
			print("\t\t|| Match player at : {} ||".format(temp))
			player[0] = math.floor(check[1]/10)
			player[1] = (check[1]%10)
			temp = player[0]*10+player[1]
			if check[0] > check[1]:
				print("\t\t|| Got Bitten By Snake ||")
			else:
				print("\t\t|| Yayy!! Found A Ladder ||")

			print("\t\t|| Player Moved To  {} ||".format(temp))
			print("\n\n\t\t==================================\n\n")

	return player






game(player)