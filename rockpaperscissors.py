# ~ ROCK PAPER SCISSORS ~
# 
# This is a simple program I wrote to get warmed back up into programming after taking some time off.
# It allows the user to play Rock, Paper, Scissors with a single opponent, track how many points they
# have collected and tells the winner if they lose or win.
#
# Author: Bethany Grentz
# Date: August 17, 2025
# Version: 1.0


# Desired Imports
import random

# Setup player initial tracking
mainUserPoints = 0
compUserPoints = 0

# Prepare hands: 0 = Rock, 1 = Scissors, 2 = Paper
mainUserHand = 0
compUserHand = 0
mainUserHandCheck = False

# Hand Dictionary
handDict = {
    0: "Rock",
    1: "Scissors",
    2: "Paper"
}

# Setup loop
while (compUserPoints < 3 and mainUserPoints < 3):

    # Reset the userHand check
    mainUserHandCheck = False

    # Set the computer's hand:
    compUserHand = random.randrange(1,3)

    # Set the main user's hand:
    while mainUserHandCheck is False:

        # Prompt the user for their preferred hand
        print("\nPlease provide your hand: 0 = Rock, 1 = Scissors, 2 = Paper")
        mainUserHand = input()

        # Check with user the valid hand
        if mainUserHand == "0":
            print("You selected Rock!")
            mainUserHandCheck = True
        elif mainUserHand == "1":
            print("You selected Scissors!")
            mainUserHandCheck = True
        elif mainUserHand == "2":
            print("You selected Paper!")
            mainUserHandCheck = True
        else: 
            print("That is not a valid hand, please try again with an integer.")

    # Inform user opponent's selection
    print(f"Your opponent selected {handDict[compUserHand]}!")

    # When opponent rolls Rock
    if compUserHand == 0:
        if int(mainUserHand) == 0:
            print(f"You both rolled {handDict[compUserHand]}, try again!")
        if int(mainUserHand) == 1:
            print("Darn! Rock beats Scissors, your opponent gains a point.")
            compUserPoints = compUserPoints + 1
        if int(mainUserHand) == 2:
            print("Nice! Rock beats Paper, you gain a point!")
            mainUserPoints = mainUserPoints + 1

    # When opponent rolls Scissors
    if compUserHand == 1:
        if int(mainUserHand) == 1:
            print(f"You both rolled {handDict[compUserHand]}, try again!")
        if int(mainUserHand) == 0:
            print("Nice! Rock beats Scissors, you gain a point!")
            mainUserPoints = mainUserPoints + 1
        if int(mainUserHand) == 2:
            print("Darn! Scissors beats Paper, your opponent gains a point.")
            compUserPoints = compUserPoints + 1

    # When opponent rolls Paper
    if compUserHand == 2:
        if int(mainUserHand) == 2:
            print(f"You both rolled {handDict[compUserHand]}, try again!")
        if int(mainUserHand) == 0:
            print("Darn! Paper beats Rock, your opponent gains a point.")
            compUserPoints = compUserPoints + 1
        if int(mainUserHand) == 1:
            print("Nice! Scissors beats Paper, you gain a point!")
            mainUserPoints = mainUserPoints + 1
    
    # Notify player of points
    print(f"\nYou now have {mainUserPoints} point(s)!")
    print(f"Your opponent now has {compUserPoints} point(s)!")

# If out of the loop select the winner
if (compUserPoints > mainUserPoints):
    print("\n\nToo bad! You lost the game :(")
if (compUserPoints < mainUserPoints):
    print("\n\nGreat job! You won the game! :)")
if (compUserPoints == mainUserPoints):
    print("\n\nOh well! You both tied! ")
