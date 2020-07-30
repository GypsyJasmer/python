# Lab 4 Dungeon Crawl


import constant as c
import random
from DungeonFunctions import *


# MAIN GAME PLAY
def main():
    # ALGORITHM
    inPlay = True
    size = (c.MAX_ROW, c.MAX_COL)  # default map
    print("The default dungeon size is, ", size)
    while inPlay:
        userChoice = userDefinedSize()  # returns a true if user wants to set their own size
        if userChoice:
            size = getSize()
            # testing print
            print("User dungeon size is: ", size)
            # print(type(size))  # shows the variable data type.
            # testing print
            dungeon = createMap(size[0], size[1])  # places the size of the map as int #1=index 0 and int #2 = index 1
        else:
            dungeon = createMap()  # default parameters
        gamePlay = True
        # finding player location
        playerLocation = findPlayer(dungeon, size[0], size[1])
        print(playerLocation)
        while gamePlay:
            # while move==SPACE we can keep playing.
            # displaying current dungeon
            displayDungeon(dungeon)
            ###GET MOVE WORKS, however I need a loop to keep going while a valid move can be made.
            move = getMove(size[0], size[1], playerLocation)
            win = checkWin(dungeon, move, playerLocation)
            lost = checkLose(dungeon, move, playerLocation)
            # testing if inPlay is still True vai CheckQuit
            inPlay = checkQuit(move)
            if not inPlay:
                continue
            playerLocation = updateMap(dungeon, playerLocation, move)
            if win:
                print("You found the treasure!")
                gamePlay = False
            elif lost:
                print("You stepped on a trap, you lost")
                gamePlay = False
            else:
                # if true that means there is a space available
                gamePlay = True
            if not gamePlay:
                play = repeat()
                if play:
                    inPlay = True
                else:
                    inPlay = False
                    print("See ya later suckah!")


if __name__ == "__main__":
    main()
# include guards actually calling the main function
