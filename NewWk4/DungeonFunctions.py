# Functions
import constant as c
import random


# should be used any place the user is required to select yes or no
# should return true for yes and false for no.
def validYesNo(Input):
    isValid = False
    userInput = ""
    while userInput != "Y" and userInput != "N":
        userInput = input(Input).upper()  # prompt the user for actual input
    if userInput == "Y":
        isValid = True

    return isValid


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
    return validYesNo("Would you like to set the size of your dungeon \n" +
                      " or go with the preset size 10x12? \n" +
                      "Y to create your own size or any button for no. \n")


# return a tuple for the user requested dungeon size
def getSize():
    width = int(input("Enter the width of the dungeon"))
    height = int(input("Enter the height of the dungeon"))
    return width, height


# this function will create the 2D list for the map and return it to
# main after it has been created . This can be called with default
# values for the default size, or with custom values from getSize
def createMap(width=c.MAX_ROW, height=c.MAX_COL):
    dungeonMap = []  # Make initial list
    for row in range(height):  # for every row
        dungeonMap.append([])  # make a new list
        dungeonMap[row] = [c.SPACE] * width  # fill the list spaces all at once
        # tester
        # print("Dungeon is set")
    placeTrap(dungeonMap, width, height)
    placeTreasure(dungeonMap, width, height)
    placePlayer(dungeonMap, width, height)

    return dungeonMap  # created Map


# displays the map layout
def displayDungeon(dungeonMap):
    print("Here is what the dungeon currently looks like")
    for row in dungeonMap:
        for col in row:
            print(col, end="")
        print()  # this moves the row down


# These place functions:  should be called from within createMap
# and should take the map and number of each thing being
# placed into the map and place the appropriate number of
# objects randomly into the map. Default parameters should
# be defined in constant.py and specified in function definition
def placeTrap(dungeonMap, width, height):
    for index in range(c.NUM_TRAPS):
        # this is the empty space tuple
        trapSpots = findEmpty(dungeonMap, width, height)
        dungeonMap[trapSpots[0]][trapSpots[1]] = c.TRAP

    # print("Traps are set")


def placeTreasure(dungeonMap, width, height):
    for index in range(c.NUM_CASH):
        cashSpots = findEmpty(dungeonMap, width, height)
        # this is the empty space tuple
        dungeonMap[cashSpots[0]][cashSpots[1]] = c.CASH
    # print("Treasure is set")


def placePlayer(dungeonMap, width, height):
    # this is the empty space tuple
    playerSpot = findEmpty(dungeonMap, width, height)
    dungeonMap[playerSpot[0]][playerSpot[1]] = c.PLAY
    print("This is the player location from place PLayer:", playerSpot)
    # print("Player is set")


# def placeMonster(dungeonMap, width, height):
#     # this is the empty space tuple
#     monsterSpot = findEmpty(dungeonMap, width, height)
#     dungeonMap[monsterSpot[0]][monsterSpot[1]] = c.MONSTER



# this method will be used in createMap. When called, it will
# find a random location on the map that is empty and return
# a tuple (row, column) for that location
def findEmpty(dungeonMap, width, height):
    emptySpot = False
    while not emptySpot:
        row = random.randrange(height)
        col = random.randrange(width)
        if dungeonMap[row][col] != c.SPACE:
            emptySpot = False
        else:
            return row, col  # returns the tuple


#
# this function will find the player location on the map and return
# a tuple (row, column) of where it is
# does not track player just searches the board.
def findPlayer(dungeonMap, width, height):
    # bool for player
    found = False
    while not found:
        for row in range(height):  # scans rows
            for col in range(width):  # scans col
                if dungeonMap[row][col] != c.PLAY:  # checks player
                    found = False  # once found breaks out of loop and return row and column.
                else:
                    return row, col


# this function should get a move from the player and return a
# tuple containing the new location of the player.
# This function should only return a move after validating that it
# is within the array. The player should also be allowed
# choose the letter q to quit the game and return (-1, -1) to main
def getMove(width, height, playerLocation):
    validMove = False
    move = ()
    while not validMove:
        playerMove = input("Enter 'U' for Up, 'D' for Down, 'L' for Left, and 'R' for Right and Q for Quit").upper()
        if playerMove != 'U' and playerMove != 'D' and playerMove != 'L' and playerMove != 'R' and playerMove != 'Q':
            print("please enter U, D, L, R, or Q")
        else:
            if playerMove == c.UP:
                move = -1, 0
            elif playerMove == c.DOWN:
                move = 1, 0
            elif playerMove == c.LEFT:
                move = 0, -1
            elif playerMove == c.RIGHT:
                move = 0, 1
            elif playerMove == c.QUIT:
                move = -1, -1
            inbounds = checkBounds(playerLocation, move, width, height)
            if inbounds:
                validMove = True
    # print(move)
    return move


# if the player has chosen to quit the game, this should be used to
# terminate the game loop without the use of break
def checkQuit(move):
    if move[0] == -1 and move[1] == -1:
        return False
    return True


# this function should be called inside of getMove and validate
# whether or not the player has attempted to move outside of the
# bounds of the list.
def checkBounds(playerLocation, move, width, height):
    inBounds = False
    while not inBounds:
        # left and up
        if playerLocation[0] + move[0] < 0 or playerLocation[1] + move[1] < 0 or \
                playerLocation[0] + move[0] > width - 1 or playerLocation[1] + move[1] > height - 1:
            print("Out of bounds")
            return False
        return True


# these functions should accept the map and move and test
# whether the chosen move will cause the player to win or lose
# the game. Should return true or false. Should not update the
# the map. The result of these should be used to terminate the
# game loop without the use of break
def checkWin(dungeonMap, move, playerLocation):
    isWin = False
    while not isWin:
        if dungeonMap[playerLocation[0] + move[0]][playerLocation[1] + move[1]]  == c.CASH:
            isWin = True
        return isWin


def checkLose(dungeonMap, move, playerLocation):
    isLost = False
    while not isLost:
        if dungeonMap[playerLocation[0] + move[0]][playerLocation[1] + move[1]] == c.TRAP:
            isLost = True
        return isLost


# this function should accept the map and move from main and
# use them to update the Map. You should not update the map
# unless not win and not lose.
# a) pass in the dungeon and the move
# b) update the dungeon moving the player marker(place a new player and clear the old spot)
# c) return type should be void
def updateMap(dungeonMap, playerLocation, move):
    dungeonMap[playerLocation[0]][playerLocation[1]] = c.SPACE
    # this creates a new tuple by adding the old tuple together for the current spot.
    playerLocation = (playerLocation[0] + move[0], playerLocation[1] + move[1])
    # then this creates the new spot for the player
    dungeonMap[playerLocation[0]][playerLocation[1]] = c.PLAY

    return playerLocation


# after the game is over, this function should see if the player
# wishes to start again. Should return true or false. Should use
# validYesNo. If the user wants to play again, start over with a
# new dungeon
def repeat():
    return validYesNo("Do you want to play again? Y for Yes any other key for No")


if __name__ == "__main__":
    displayInstructions()

    getMove(10, 10, (2, 2))
