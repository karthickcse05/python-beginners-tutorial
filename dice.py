import random


class Dice:
    def roll(self):
        first = random.randint(1,12)
        second= random.randint(1,12)
        return first,second


dice=Dice()
print(dice.roll())

