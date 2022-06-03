# import random module
import random

# Printing The Game Instructions

print("Winning Rules of the Rock paper scissor game as follows: \n"
      + "Rock vs paper->paper wins \n"
      + "Rock vs scissor->Rock wins \n"
      + "paper vs scissor->scissor wins \n")

# The game is in a loop to allow players play for as long as they want
while True:
    print("Enter choice \n r for Rock, \n p for paper, and \n s for scissors \n")

    # Taking input from user
    choice = str(input("User turn: "))

    # corresponding to the choice value
    if choice == 'r':
        choice_name = 'Rock'
    elif choice == 'p':
        choice_name = 'paper'
    else:
        choice_name = 'scissors'

    # Printing the players choice
    print("user choice is: " + choice_name)
    print("\nNow its computer turn.......")

    # Computer randomly chooses rock,paper or scissors

    options = ["rock", "paper", "scissors"]
    comp_choice = random.choice(options)

    # looping until comp_choice value
    while comp_choice == choice:
        comp_choice = random.choice(options)

    # initializing the value of comp_choice_name

    if comp_choice == "rock":
        comp_choice_name = 'Rock'
    elif comp_choice == "paper":
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'

    print("Computer choice is: " + comp_choice_name)

    print(choice_name + " V/s " + comp_choice_name)

    # Writing Out The Conditions for Winning

    #Setting conditions for a Tie
    if ((choice == "r" and comp_choice == "rock") or
            (choice == "p" and comp_choice == "paper") or
            (choice == "s" and comp_choice == "scissors")):
        print("Its a Tie")

    elif ((choice == "r" and comp_choice == "paper") or
            (choice == "p" and comp_choice == "rock")):
        print("paper wins => ", end="")
        result = "paper"

    elif ((choice == 'r' and comp_choice == 'scissors') or
          (choice == "s" and comp_choice == "rock")):
        print("Rock wins =>", end="")
        result = "Rock"

    else:
        print("scissor wins =>", end="")
        result = "scissor"

    # Printing either user or computer wins
    if result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")

    print("Would you like to play again? (Y/N)")
    ans = input()

    # if user input n or N then condition is True
    if ans == 'n' or ans == 'N':
        break

# After Breaking the loop
print("\nThanks for playing")