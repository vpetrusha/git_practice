
import random

home_team = int(input("Enter home team rating [1-10]:"))
away_team = int(input("Enter away team rating [1-10]:"))
form_home = int(input("Enter home team form value:"))
form_away = int(input("Enter away team form value:"))
ratio = 4

dice_roll_home = (home_team + form_home + ratio) 
dice_roll_away = (away_team + form_away + ratio)

def dice_roll():
	dice_roll_home_list = []
	dice_roll_away_list = []
	for _ in range(dice_roll_home, dice_roll_away):
		dice_roll_home_list.append(random.randint(1, 6))
		dice_roll_away_list.append(random.randint(1,6))
	print(f"The probable score is {dice_roll_home_list.count(6)} : {dice_roll_away_list.count(6)}")


dice_roll()