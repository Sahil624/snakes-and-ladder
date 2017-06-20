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
	print("Game called")

	while player != (100,100):

		input("Press Enter For Next Move")

		x=player[0]
		y=player[1]

		no = x*10+y
	
		dice = throw_dice()
		print("Dice Gives ",dice)

		if no == 100 :
			print("Exceeding 100")
			break	

		if no+dice > 100 and no + dice != 100 :
			game(player)

			

		y=y+dice

		if y>10 :
			y=y+dice-10
			x=x+1

		player[0] = x
		player[1] = y
		player = check_pos(player)


def throw_dice():
	return random.randint(1,6)

def check_pos(player):
	temp = player[0]*10+player[1]
	print("player",temp)
	# player_pos = 
	for check in bad:
		if temp == check[0]:
			print("\t\tMatch player at : {}".format(temp))
			player[0] = math.floor(check[1]/10)
			player[1] = (check[1]%10)
			temp = player[0]*10+player[1]
			if check[0] > check[1]:
				print("\t\tGot Bitten By Snake ")
			else:
				print("\t\tYayy!! Found A Ladder")

			print("\t\tPlayer Moved To ",temp)

	return player






game(player)