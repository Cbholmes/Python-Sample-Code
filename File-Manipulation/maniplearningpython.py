
with open("learningpython.txt") as file:
  #reads the file then prints it
  print(file.read())
  print()
  #goes back to the begining of the file
  file.seek(0)
  #uses a loop to go through each line in the file and prints it
  for i in file:
    print(i, end="")
  print('\n')
  file.seek(0)
  #creates a list with each item corresponding to each line in the file then prints each item in the list
  messages = file.read().splitlines()
for i in messages:
  print(i)
print()


with open("learningpython.txt", r+) as file:
  #creates a list with each line in the file then edits each item in the list to replace "Python" with "JavaScript" 
  messages = file.readlines()
  for i in range(len(messages)):
    messages[i] = messages[i].replace("Python", "JavaScript")
  file.seek(0)
  #writes the new list into the file then prints the file to screen
  file.writelines(messages)
  file.seek(0)
  for i in file.read().splitlines():
    print(i)
