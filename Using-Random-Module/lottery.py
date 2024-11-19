from random import choice
"""
File name: lottery.py
Module makes a random list of 5 letters and 10 numbers then picks 4 winning characters from the list.
"""
def main():
    """Driver Code sets testlist to return value of makeList() then calls getWinner()"""
    testlist = makeList()
    print("Potential winning letters/numbers:", testlist)
    getWinner(testlist)

def makeList():
  """Creates a list of 5 random letters and 10 random numbers"""
  potchars = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
  reslist = []
  for i in range(10):
    reslist.append(choice(range(10)))
  for i in range(5):
    reslist.insert(choice(range(len(reslist))), choice(potchars))
  return reslist

def getWinner(testlist):
  """Gets 4 random items from the test list then prints a message saying whoever ticket matches those 4 items wins"""
  temp = testlist[:]
  winnums = ""
  for i in range(3):
    num = choice(temp)
    winnums += str(num) + ", "
    temp.pop(temp.index(num))
  winnums += "and " + str(choice(temp))
  print("If your ticket matches the letters/numbers", winnums + ", you win.\n")

if __name__ == "__main__":
  main()
