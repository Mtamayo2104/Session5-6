# you have three lives, you roll a dice, if you get a 6 you win
# if you dont get a 6, you lose 1 life
from random import randint

lives = 3
while lives > 0: # as long as i have more lives
    # roll the dice
    dice = randint(1,6)
    if dice == 6:
        print("you rolled a 6, you win!")
        break
    lives = lives -1
    print("you rolled a", dice, "you have", lives, "lives left")

if lives ==0:
    print('you lose!')
