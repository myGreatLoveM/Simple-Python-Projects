import random #random module

rolls = ['''
-------
|     |
|  0  |
|     |
-------''', '''
-------
|    0|
|     |
|0    |
-------''', '''
-------
|    0|
|  0  |
|0    |
-------''', '''
-------
|0   0|
|     |
|0   0|
-------''', '''
-------
|0   0|
|  0  |
|0   0|
-------''', '''
|0 0 0|
|     |
|0 0 0|''']

input("Press the Enter to Start:")

die1 = random.randint(0,5)
die2 = random.randint(0,5)
print('')

print(f"Player1 has : {rolls[die1]}\nvs\nPlayer2 has: {rolls[die2]}")
print('')

if (die1 > die2):
  print("Player1 has won the Game.")
elif (die1 < die2):
  print("Player2 has won the Game.")
else :
  print("It is Draw!")
  