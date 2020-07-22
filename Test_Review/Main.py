# rock paper scissors

import random
import const as c
from Functions import *


def main():
    userChoice = ""
    computerChoice = 0
    # sets the score at 0 to start the game.
    userWins = 0
    computerWins = 0
    displayInstructions()
    userChoice = GetUserChoice()
    # computerChoice = GetUserChoice()
    # DisplayComputerChoice(computerChoice)
    #
    # winner = DetermineWinner(userChoice, computerChoice)
    # displayWinner(winner)
    # IncrementScores(winner, userWins, computerWins)
    # print("Your won:{0} ".format(userWins))
    # print("Computer won: {1}".format(computerWins))


if __name__ == "__main__":
    main()
# include guards actually calling the main function
