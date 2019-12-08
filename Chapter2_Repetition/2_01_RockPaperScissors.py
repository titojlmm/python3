import random

# This program plays the game known as Rock-Paper-Scissors.
# Programmed by J. Parker Jan-2017
print("Rock-Paper_Scissors is a simple guessing game.")
print("The computer will prompt you for your choice, ")
print("which must be one of 'rock', 'paper', or 'scissors'")
print("When you select a choice the computer will too (it ")
print("will not cheat) and the winner is selected by three ")
print("simple rules: rock beats scissors, paper beats ")
print("rock, and scissors beat paper. If a tie happens")
print("then you should play again.")

# Computer selection
i = random.randint(1, 3)
if i == 1:
  choice = "rock"
elif i == 2:
  choice = "paper"
else:
  choice = "scissors"

print("Rock-paper-scissors: type in your choice: ")
player = input()

if player == choice:
  print("Game is a tie. Please try again.")
else:
  if player == "rock":
    if choice == "scissors":
      print("Congratulations. You win.")
    else:
      print("Sorry. Computer wins")
  elif player == "paper":
    if choice == "rock":
      print("Congratulations. You win.")
    else:
      print("Sorry. Computer wins")
  elif player == "scissors":
    if choice == "paper":
      print("Congratulations. You win.")
    else:
      print("Sorry. Computer wins")
  else:
    print("Option ", player, " is not valid. Please choose among rock, paper or scissors")
