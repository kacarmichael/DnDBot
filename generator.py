import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import random

SIMULATION_LENGTH = 1000

class dice_set:
    def __init__(self, sides: list):
        self.sides = sides

    def roll(self):
        pass
    
    @property
    def min(self):
        pass

    @property
    def max(self):
        pass

def roll_die(sides: int):
    return random.randint(1, sides)

def roll(dice: dict, modifier: int = 0):
    roll = []
    for key, value in dice.items():
        for i in range(value):
            roll.append(roll_die(key))
    return sum(roll) + modifier

def freq(rolls: list):
    freq = {}
    for roll in rolls:
        if roll in freq:
            freq[roll] += 1
        else:
            freq[roll] = 1
    return freq

#Dict of number of sides:number of dice
def simulation(dice: dict, modifier: int = 0):
    rolls = []
    for i in range(SIMULATION_LENGTH):
        rolls.append(roll(dice, modifier))
    return rolls

#Example: 3 d6
if __name__ == "__main__":
    print(simulation({6:3}))
