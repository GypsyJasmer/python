# Functions

import random
import const as c


def displayInstructions():
    print("We're going to play Rock, Paper, Scissors")


def GetUserChoice():
    userChoice = ""  # string
    while userChoice != "R" and userChoice != "P" and userChoice != "S":
        userChoice = input("Please enter R for Rock, P for Paper, or S for Scissors")
        userChoice.upper()
    return userChoice


def GetComputerChoice():
    randGen = random.randrange(1, 4)
    return randGen


def DisplayComputerChoice(computerChoice):
    if computerChoice == c.ROCK:
        print("The computer chose ROCK")
    elif computerChoice == c.PAPER:
        print("The computer chose PAPER")
    else:
        print("The computer chose SCISSORS")


def DetermineWinner(userChoice, computerChoice):
    if ((userChoice == "R" and computerChoice == c.ROCK) or
            (userChoice == "P" and computerChoice == c.PAPER) or
            (userChoice == "S" and computerChoice == c.SCISSORS)):
        return c.TIE
    elif ((userChoice == "R" and computerChoice == c.SCISSORS) or
          (userChoice == "P" and computerChoice == c.ROCK) or
          (userChoice == "S" and computerChoice == c.PAPER)):
        return c.USERWON
    else:
        return c.COMPTUERWON


def displayWinner(winner):
    if winner == c.USERWON:
        print("You Won!")
    elif winner == c.COMPTUERWON:
        print("The Computer Won!")
    else:
        print("It's a tie")


def IncrementScores(winner, userWins, computerWins):
    if winner == c.USERWON:
        userWins = userWins + 1
    elif winner == c.COMPTUERWON:
        computerWins = computerWins + 1


def validYesNo(Input):
    isValid = False
    userInput = ""
    while userInput != "Y" and userInput != "N":
        userInput = input(userInput).upper()  # prompt the user for actual input
    if userInput == "Y":
        isValid = True

    return isValid


def repeat():
    return validYesNo("Do you want to play again? Y for Yes any other key for No")
