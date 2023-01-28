# initializing the Global variables

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


# tells us whether the game is going or not?
game_in_play = True

# the variable for defining who the winner will be
winner = None

# this is the player who'll be playing the chance
player_playing = "X"

# defining the functions for the game

# to start the game


def link_start():

    # to display the tic tac board
    project_board()

    # finite loop till the game is decided
    while game_in_play:

        # to manage the turn each player is taking
        turn_master(player_playing)

        # to check if the game is over or not
        is_game_over()

        # changing_turn for each player
        change_turn()

    # to specify whether the decision of the game is a win or tie
    if winner == "X" or winner == "O":
        print(winner + ", won")
    else:
        print("It's a tie, better luck next time..")


# Display the board with the specific positions for making the user comfortable with the game
def project_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "        1|2|3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "        4|5|6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "        7|8|9")
    print("\n")


# handling the turn for the player
def turn_master(ttc_player):

    # get coordinates from the player
    print(ttc_player + ", your turn")
    coordinates = input("Take a position from 1-9 = ")

    # to verify that the coordinates are valid or not
    validity = False
    while not validity:

        # to check the validity
        possible_positions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        while coordinates not in possible_positions:
            coordinates = input("Take a position from 1-9 = ")

        # to convert the coordinates for indexing
        coordinates = int(coordinates) - 1

        # to avoid overwriting of the marked positions
        if board[coordinates] == "-":
            validity = True
        else:
            print("The position is already occupied, choose another location")

    # marks the specified position on the board
    board[coordinates] = ttc_player

    # shows the board with the player's marker marked
    project_board()

# to check the decision of the game


def is_game_over():
    is_it_win()
    is_it_tie()

# to check if the game has been decided or not


def is_it_win():
    global winner

    # check the winner in any way
    row_win = see_row()
    column_win = see_column()
    diagonal_win = see_diagonal()

    # specify the winner
    if row_win:
        winner = row_win
    elif column_win:
        winner = column_win
    elif diagonal_win:
        winner = diagonal_win
    else:
        winner = None

# how to check the rows


def see_row():
    global game_in_play

    # checks if any of the row follows the following combinations
    row_1 = board[0] == board[1] == board[3] != "-"
    row_2 = board[4] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_in_play = False

    # return the winner row
    if row_1:
        return board[0]
    elif row_2:
        return board[4]
    elif row_3:
        return board[6]
    # if no winner
    else:
        return None

# how to check the columns


def see_column():
    global game_in_play

    # checks if any of the column follows the following combinations
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_in_play = False

    # return the winner column
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    # if no winner
    else:
        return None

# how to check the diagonals


def see_diagonal():
    global game_in_play

    # checks if any of the diagonals follows the following combinations
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2:
        game_in_play = False

    # return the winner row
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[4]

    # if no winner
    else:
        return None


# checks if the game is a tie
def is_it_tie():
    global game_in_play

    # if the board is full
    if "-" not in board:
        game_in_play = False
        return True

    # if the board is not full
    else:
        return False


# changing each player's turn


def change_turn():
    global player_playing

    # if the current player is playing with the marker as X
    if player_playing == "X":
        player_playing = "O"

    # if the current player is playing with the marker as O
    elif player_playing == "O":
        player_playing = "X"


# Let The Games Begin........

link_start()

