# IS it better to pick random numbers or specfic numbers each time you play the lottery


    # Rules
        # Must pick 6 numbers
        # 5 are different numbers from 1 - 70
        # 1 number from 1- 25
import math
import random

white_balls = list(range(1,71))
gold_balls = list(range(1,26))


def lottery(my_numbers):
    win_white = random.choices(white_balls,k=5)
    win_gold = random.choices(gold_balls,k=5)
    my_numbers_white = my_numbers[0:6]
    my_numbers_gold = my_numbers[5]

    for i in my_numbers_white:
        if i in win_white and my_numbers_gold==win_gold:
            win = 1
        else:
            win = 0
            break

    return win

# my_numbers = random.sample(white_balls,5)+random.sample(gold_balls,1)

wins = 0
for i in range(10000000):
    my_numbers = random.sample(white_balls, 5) + random.sample(gold_balls, 1)
    wins += lottery(my_numbers)

print('You have won '+str(wins)+' times after 300,000,000 games')