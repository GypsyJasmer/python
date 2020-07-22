# Functions
import constant as c
import random


# this function will display the instructions for playing this game
def displayInstructions():
    first_play = False
    if not first_play:
        print("Welcome to Dungeon Crawl! \n" +
              "The goal is to get to the exit of the \n" +
              "dungeon without hitting any of the traps. \n" +
              "Best of luck to you! \n")
    else:
        print("You know how to play Dungeon Crawl, get crawling.")


# this function should return true if the user wants to define the dungeon size
def userDefinedSize():
    userChoice = False
    print("Would you like to set the size of your dungeon \n" +
          " or go with the preset size 10x12? \n")
    answer = input("Y to create your own size or any button for no. \n")
    answer = answer.upper()
    if answer == 'Y':
        userChoice = True
    return userChoice


# return a tuple for the user requested dungeon size
def getSize():
    width = int(input("Enter the width of the dungeon"))
    height = int(input("Enter the height of the dungeon"))
    return width, height


#this function will create the 2D list for the map and return it to
#main after it has been created . This can be called with default
#values for the default size, or with custom values from getSize
def createMap(width, height):
    pass
# #should be used any place the user is required to select yes or no
# #should return true for yes and false for no.
# def validYesNo():
#
# #These place functions:  should be called from within createMap
# #and should take the map and number of each thing being
# #placed into the map and place the appropriate number of
# #objects randomly into the map. Default parameters should
# #be defined in constant.py and specified in function definition
# def placeTrap(map, numTraps):
#
# def placeTreasure(map, numTreasure):
#
# def placePlayer(map):
#
# this method will be used in createMap. When called, it will
# find a random location on the map that is empty and return
# a tuple (row, column) for that location
def findEmpty(map, width, height):
    emptySpot = False
    while not emptySpot:
        row = random.randrange(height)
        col = random.randrange(width)
        if map[row][col] != c.SPACE:
            emptySpot = False
        else:
            return row, col
#
# #this function will find the player location on the map and return
# #a tuple (row, column) of where it is
# def findPlayer(map):
#
# #this function should get a move from the player and return a
# #tuple containing the new location of the player.
# #This function should only return a move after validating that it
# #is within the array. The player should also be allowed
# #choose the letter q to quit the game and return (-1, -1) to main
# def getMove(map):
#
#
# #if the player has chosen to quit the game, this should be used to
# #terminate the game loop without the use of break
# def checkQuit(move):
#
#
# # this function should be called inside of getMove and validate
# #whether or not the player has attempted to move outside of the
# #bounds of the list.
# def checkBounds(map, move):
#
# #these functions should accept the map and move and test
# #whether the chosen move will cause the player to win or lose
# #the game. Should return true or false. Should not update the
# #the map. The result of these should be used to terminate the
# #game loop without the use of break
# def checkWin(map, move):
#
# def checkLose(map, move):
#
# #this function should accept the map and move from main and
# #use them to update the Map. You should not update the map
# #unless not win and not lose.
# def updateMap(map, move):
#
#
# #after the game is over, this function should see if the player
# #wishes to start again. Should return true or false. Should use
# #validYesNo. If the user wants to play again, start over with a
# #new dungeon
# def repeat():
#     go_again = False
#     answer = ''
#     while answer != 'Y' and answer != 'N':
#         answer = input("Do you want to play again? Y for Yes any other key for No")
#         answer = answer.upper()
#         if answer == 'Y':
#             go_again = True
#     return go_again
