# Lab 4 Dungeon Crawl


import constant as c
import random
from Dungeon_Functions import *


# MAIN GAME PLAY
def main():
    # ALGORITHM
    print("is this working?")
    inPlay = True
    size = (c.MAX_ROW, c.MAX_COL)  # default map
    print("The default dungeon size is, ", size)
    # while inPlay:
    #     userChoice = userDefinedSize()  # returns a true if user wants to set their own size
    #     if userChoice:
    #         size = getSize()
    #         # testing print
    #         print("User dungeon size is: ", size)
    #         print(type(size))  # shows the variable data type.
    #         # testing print
    #         dungeon = createMap(size[0], size[1])  # places the size of the map as int #1=index 0 and int #2 = index 1
    #     else:
    #         dungeon = createMap()  # default parameters

    if __name__ == "__main__":
        main()
