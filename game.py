import random
import math

x=0
y=0

bad = [(17,7),(54,34),(64,60),(62,19),(87,24),(93,73),(95,75),(99,78)]

player = [0,0]

def game(player):
	print("Game called")
	while player != (100,100):

		x=player[0]
		y=player[1]

		no = x*10+y

		if(no>100):
			print("Exceeding 100")
			break

		dice = throw_dice()
		print("Dice Gives ",dice)
		

		y=y+dice

		if y>10 :
			y=y+dice-10
			x=x+1

		player[0] = x
		player[1] = y
		player = check_pos(player)

		input("Press Enter For Next Move")


def throw_dice():
	return random.randint(1,6)

def check_pos(player):
	print("player",player)
	temp = player[0]*10+player[1]

	for check in bad:
		if temp == check[0]:
			print("\t\tMatch player at : {} Temp is {}".format(player,temp))
			player[0] = math.floor(check[1]/10)
			player[1] = (check[1]%10)
			print("\t\tPlayer Moved To ",player)

	return player






game(player)