from ranom import choice
"""
File name: dieroll.py
Module contains a die class that can get a random number from 1 to the ammount of sides in the die
"""

class Die():
  """Class represents a die"""
  
  def __init__(self, sides=6):
    """Constructor creates a die with given ammount of sides"""
    self._sides = sides

  def rollDie(self):
    """gets a random number from 1 to the amount of sides in the die and then prints that number"""
    roll = choice(range(1, self._sides+1))
    print("Rolled a", roll)
