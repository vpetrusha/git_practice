
import random

home_team = int(input("Enter home team rating [1-10]:"))
away_team = int(input("Enter away team rating [1-10]:"))
form_home = int(input("Enter home team form value:"))
form_away = int(input("Enter away team form value:"))
ratio = 4

dice_roll_home = (home_team + form_home + ratio) 
dice_roll_away = (away_team + form_away + ratio)

list_home = []

for _ in range(dice_roll_home):
	list_home.append(random.randint(1, 6))
print(list_home)

list_away = []

for _ in range(dice_roll_away):
	list_away.append(random.randint(1, 6))
print(list_away)

print(f"The probable score is {list_home.count(6)} : {list_away.count(6)}")