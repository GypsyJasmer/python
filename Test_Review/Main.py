# rock paper scissors

import random
import const as c
from Functions import *


def main():
    play_again = True
    # sets the score at 0 to start the game.
    userWins = 0
    computerWins = 0
    displayInstructions()
    while play_again:
        playGame = True
        while playGame:
            userChoice = GetUserChoice()
            computerChoice = GetComputerChoice()
            winner = DetermineWinner(userChoice, computerChoice)
            displayWinner(winner)
            IncrementScores(winner, userWins, computerWins)
            print("You've won: ", userWins, "times")
            print("Computer won: " , computerWins, "times")


if __name__ == "__main__":
    main()
# include guards actually calling the main function
