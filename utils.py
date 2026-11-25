import random


def flip_coin():
    mylist = ["Орел", "Решка"]
    return random.choice(mylist)

def roll_dice():
    return random.randint(1, 6)