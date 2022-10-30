import random

print("Welcome to the Guessing Game.")
print("You have 5 guesses.")
count = 1

number = random.randint(1,50)

for i in range(1,6):  
  userGuess = int(input("Guess a number between 1 and 50 :- "))

  if (userGuess == number):    
    if (i > 1):
      print(f"You have Guessed right in {i} in attempts.")
    else:
      print(f"You have Guessed right in first attempt.")
    break

  elif (userGuess < number):
    if ((number-userGuess) > 10) :
      print(f"Too Low. Try again and you are left with {5-i} attempts.")
    else:
      print(f"Oops near. But still low. You are left with {5-i} attempts.")

  else :
    if ((userGuess-number) > 10):
      print(f"Too High.Try again and you are left with {5-i} attempts.")
    else:
      print(f"Oops near. But still high. You are left with {5-i} attempts.")
      
  print('')

  count = count + 1

if (count == 6):
  print("Oops run out of attempts. Better luck next time.")
  print(f"Right Guess was : {number}.")