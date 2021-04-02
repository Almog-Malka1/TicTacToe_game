board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

# ----global variabels----
current_player = "X"
game_going = True
winner = None


# Display board
def display_board():
    global board
    print("\n")
    print(" ", board[0], " | ", board[1], " | ", board[2])
    print(" −−−−−−−−−−−−−−−")
    print(" ", board[3], " | ", board[4], " | ", board[5])
    print(" −−−−−−−−−−−−−−−")
    print(" ", board[6], " | ", board[7], " | ", board[8])
    print("\n")


def handle_turn(player):
    # taking info from the user
    position = input("Enter a number from 1-9: ")

    while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        position = input("Erorr, enter a number from 1-9: ")

    print("__________________________")
    position = int(position) - 1

    board[position] = player

    display_board()


# Check if the game over
def check_game_over():

    check_if_win()
    check_if_tie()


# Checking for win
def check_if_win():

    win_in_row()
    win_in_colum()
    win_in_diagonals()


def win_in_row():

    # global vars
    global game_going
    global winner

    # check per row
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1:
        game_going = False
        winner = True
    elif row_2:
        game_going = False
        winner = True
    elif row_3:
        game_going = False
        winner = True

    return


def win_in_colum():

    # globar vars
    global game_going
    global winner

    # check per colum
    colum_1 = board[0] == board[3] == board[6] != "-"
    colum_2 = board[1] == board[4] == board[7] != "-"
    colum_3 = board[2] == board[5] == board[8] != "-"

    if colum_1:
        game_going = False
        winner = True
    elif colum_2:
        game_going = False
        winner = True
    elif colum_3:
        game_going = False
        winner = True


def win_in_diagonals():

    # globar vars
    global game_going
    global winner

    # Check per colum
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1:
        game_going = False
        winner = True
    elif diagonal_2:
        game_going = False
        winner = True


def check_if_tie():

    #global var
    global game_going
    global winner

    if "-" not in board:
        game_going = False
        winner = None
    return

# Fliping between players


def flip_player():

    # global var
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


# Game running
def game_run():

    # global var
    global current_player
    global winner

    # display the board
    display_board()
    while game_going:
        handle_turn(current_player)

        check_game_over()

        flip_player()

    flip_player()

    if winner == True:
        print(current_player + "`s won.")
    elif winner == None:
        print("you got a drew.")


game_run()
