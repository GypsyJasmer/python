# Lab 3 Tic Tac Toe
from typing import List

import GlobalConst as g
from Functions import *


# MAIN GAME PLAY
def main():
    # bool to start the game
    play_again = True
    first_play = False
    # Repeat Play loop until no longer wants to play.
    while play_again:
        # call display_instructions()
        first_play = display_instructions(first_play)
        # initialize board / list #list inialization in python
        board1 = [g.SPACE] * 9
        # # bool
        # win = False
        # tie = False
        # char this sets the player to start at X and will swap to O
        player = g.X
        playing = True
        # repeats while not win or draw
        while playing:
            # call show_board
            display_board(board1)
            # call get_move
            get_move(board1, player)
            # call check_win
            winner = check_win(board1)
            # call check_draw
            tie = check_draw(board1)
            # if not win or draw
            if winner == False and tie == False:
                # swap player nested in the if not win or draw
                if player == g.X:
                    player = g.O
                else:
                    player = g.X
            # say whether win or draw
            elif winner:
                print("{0} is the winner! ".format(player))
                playing = False
            elif tie:
                print("Tie Game no winners!!")
                playing = False
            # ask to play again
        play_again = repeat()


if __name__ == "__main__":
    main()
