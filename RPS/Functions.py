# Functions

import random
import const as c


def displayInstructions():
    print("We're going to play Rock, Paper, Scissors")


def GetUserChoice():
    validMove = False
    while not validMove:
        userChoice = int(input("Please enter rock(1), paper(2) or scissors(3)."))
        if userChoice < c.ROCK or userChoice > c.SCISSORS:
            print("Please enter rock(1), paper(2) or scissors(3).")
        else:
            if userChoice == c.ROCK:
                print("You chose: Rock\n")
            elif userChoice == c.PAPER:
                print("You chose: Paper\n")
            elif userChoice == c.SCISSORS:
                print("You chose: Scissors\n")
            else:
                print("Not vaild we shouldn't see this")
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
    if ((userChoice == c.ROCK and computerChoice == c.ROCK) or
            (userChoice == c.PAPER and computerChoice == c.PAPER) or
            (userChoice == c.SCISSORS and computerChoice == c.SCISSORS)):
        return c.TIE
    elif ((userChoice == c.ROCK and computerChoice == c.SCISSORS) or
          (userChoice == c.PAPER and computerChoice == c.ROCK) or
          (userChoice == c.SCISSORS and computerChoice == c.PAPER)):
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


def UserIncrementScores(userWins):
    return userWins + 1


def computerIncrementScores(computerWins):
    return computerWins + 1


def validYesNo(user_input):
    userInput = ""
    while userInput != "Y" and userInput != "N":
        userInput = input(user_input).upper()  # prompt the user for actual input
    if userInput == "Y":
        return True
    return False


def repeat():
    return validYesNo("Do you want to play again? Y for Yes any other key for No")
