# Functions

import random
import const as c


def displayInstructions():
    print("We're going to play Rock, Paper, Scissors")


def GetUserChoice():
    validMove = False
    while not validMove:
        userChoice= int(input("What is your choice?: "))
        if userChoice < c.ROCK or userChoice > c.SCISSORS:
            print("Please enter rock(1), paper(2) or scissors(3).")
        else:
            if userChoice == c.ROCK:
                print("You chose: Rock\n")
            elif userChoice == c.PAPER:
                print("You chose: Paper\n")
            elif userChoice == c.SCISSORS:
                print("You chose: Scissors\n")
            return userChoice


def GetComputerChoice():
    computerChoice = random.randrange(1, 4)
    if computerChoice == c.ROCK:
        print("Computer chose: Rock\n")
    elif computerChoice == c.PAPER:
        print("Computer chose: Paper\n")
    elif computerChoice == c.SCISSORS:
        print("Computer chose: Scissors\n")
    return computerChoice


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
