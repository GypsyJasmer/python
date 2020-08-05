# FUNCTIONS
import GlobalConst as g


# displays game instructions, #does not return anything just called in main
def display_instructions():
    first_play = False
    if not first_play:
        print("We're going to play Tic Tac Toe. This is a 2 player game. \n" +
              "Each player will choose from 1 to 9 to place X or O. Let's get going. \n")
    else:
        print("You know how to play Tic Tac Toe, place your X or O Player 1")
    first_play = True


# # initializes list to spaces
# def initialize_board(board1):
#     for i in range(len(board1)):
#         board1[i] = g.SPACE


# actually displaying the board, initialize creates the outline display to show, update moves and then display to show
def display_board(board1):
    print("Here is what the board currently looks like")
    for i in range(len(board1)):
        if board1[i] == g.SPACE:
            print("[" + str(i + 1) + "]", end="")  # just get the number not space
        else:
            print("[" + str(board1[i]) + "]", end="")
        # not part of the string of logical in the if and else above
        if (i + 1) % 3 == 0:  # this creates a new line every 3 spaces
            print(end="\n")


# pass in list board, get and validate move(in range or unoccupied square)
def get_move(board1, player):
    valid = False
    while not valid:
        move = input("{0} Enter a move between 1 and 9: ".format(player))
        if not move.isdigit():  # this validate if a digit
            print("That is an illegal move")
        else:
            position = int(move) - 1  # cast move to an int
            if position < 0 or position > 8:
                print("Please enter a valid move")
            elif board1[position] == 'X' or board1[position] == 'O':
                print("Please enter a number where there is not an existing X or O")
            else:
                # if valid move then put on board
                board1[position] = player
                valid = True


# pass in list board, return true if win
def check_win(board1):
    win = False
    # row wins
    # 1st row win
    if ((board1[0] == board1[1] and board1[1] == board1[2] and board1[0] != g.SPACE) or
            # 2nd row win
            (board1[3] == board1[4] and board1[4] == board1[5] and board1[3] != g.SPACE) or
            # 3rd row win
            (board1[6] == board1[7] and board1[7] == board1[8] and board1[6] != g.SPACE) or
            # column wins
            # 1st col win
            (board1[0] == board1[3] and board1[3] == board1[6] and board1[0] != g.SPACE) or
            # 2nd column win
            (board1[1] == board1[4] and board1[4] == board1[7] and board1[1] != g.SPACE) or
            # 3rd col win
            (board1[2] == board1[5] and board1[5] == board1[8] and board1[2] != g.SPACE) or
            # Diagonal win
            # L to R win
            (board1[0] == board1[4] and board1[4] == board1[7] and board1[0] != g.SPACE) or
            # R to L win
            (board1[2] == board1[4] and board1[4] == board1[6] and board1[2] != g.SPACE)):
        win = True

    return win


# pass in list board
def check_draw(board1):
    draw = True
    for i in range(len(board1)):
        if board1[i] == g.SPACE:
            draw = False
    return draw


def repeat():
    go_again = False
    answer = ''
    while answer != 'Y' and answer != 'N':
        answer = input("Do you want to play again? Y for Yes any other key for No")
        answer = answer.upper()
        if answer == 'Y':
            go_again = True
    return go_again
