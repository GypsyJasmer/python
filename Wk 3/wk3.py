# Lab 3 Tic Tac Toe
from typing import List

import GlobalConst as g


# FUNCTIONS
# displays game instructions, #does not return anything just called in main
def display_instructions():
    first_play = False
    if not first_play:
        print("We're going to play Tic Tac Toe. This is a 2 player game. \n" +
              "Each player will choose from 0 to 8 to place X or O. Let's get going. \n")
    else:
        print("You know how to play Tic Tac Toe, place your X or O Player 1")


# # initializes list to spaces
# def initialize_board(board1):
#     for i in range(len(board1)):
#         board1[i] = g.SPACE


# actually displaying the board, initialize creates the outline display to show, update moves and then display to show
def display_board(board):
    print("Here is what the board currently looks like")
    for i in range(len(board)):
        print("[" + str(board[i]) + "]", end="")
        if (i + 1) % 3 == 0:  # this creates a new line every 3 spaces
            print(end="\n")


# pass in list board, get and validate move(in range or unoccurpied square)
# pass in board, return a move/player choice, data validation of move choice
def get_move(board, player):
    pass


def update_board():
    pass


# returns updated board


# pass in list board,
def check_win():
    pass


# return true is win

# pass in list board
def check_draw():
    pass


# return true if tie

# playagin function
def play_again():
    pass


# MAIN GAME PLAY
def main():
    # initialize board / list
    board1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # int
    move = 0
    # bool
    win = False
    tie = False
    # char this sets the player to start at X and will swap to O
    player = g.PLAYER_X

    # Repeat PLay loop until no longer wants to play.

    # call display_instructions()
    display_instructions()
    # call initialize_player

    # play until win or draw
    # call show_board
    display_board(board1)
    # call get_move
    # call check_win
    # call check_draw
    # if not win or draw
    # swap player

    # say whether win or draw
    # ask to play again


if __name__ == "__main__":
    main()
