# rock paper scissors

import random
import const as c
from Functions import *


def main():
    first_play = True
    # sets the score at 0 to start the game.
    userWins = 0
    computerWins = 0
    tieCount = 0
    while first_play:
        displayInstructions()
        second_play = True
        while second_play:
            userChoice = GetUserChoice()
            computerChoice = GetComputerChoice()
            winner = DetermineWinner(userChoice, computerChoice)
            displayWinner(winner)
            if winner == c.USERWON:
                userWins = UserIncrementScores(userWins)
                second_play = False
            elif winner == c.TIE:
                tieCount = tieCount + 1
                second_play = False
            else:
                computerWins = computerIncrementScores(computerWins)
                second_play = False
        print("You've won: ", userWins, "times")
        print("Computer won: ", computerWins, "times")
        print("Tie games: ", tieCount, "times")
        if not second_play:
            play = repeat()
            if play:
                first_play = True
            else:
                first_play = False
                print("See ya later suckah!")


if __name__ == "__main__":
    main()
# include guards actually calling the main function
