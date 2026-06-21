CURRENT_PLAYER = 1
GAME_STATE = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

WINNING_LINES = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

EMPTY = " "

# Prints welcome message
def start_game():
    print("Welcome to Tic Tac Toe!")

# Takes in a length 9 list and prints each item in the list in a square in a Tic-Tac-Toe board
def display_grid(grid):
    for i in range(0, 9, 3):
        row = ""
        for j in range(i, i+3):
            row += " " + grid[j]
            if j < i+2:
                row += " |"
        print(row)
        if i < 6:
            print("-----------")

# Prints the game board
def display_board():
    print("\nCurrent game board:\n")

    display_grid(GAME_STATE)

# Prints the current player and the game board
def display_current_game_state():
    if CURRENT_PLAYER == 1:
        print("\nIt is Player One's (X) turn.")
    elif CURRENT_PLAYER == 2:
        print("\nIt is Player Two's (O) turn.")

    display_board()

# Asks user to input a move and places the move
def take_user_move():
    print("\nAvailable moves are shown below:\n")

    available_moves = []
    for i in range(len(GAME_STATE)):
        if GAME_STATE[i] == EMPTY:
            available_moves.append(str(i + 1))
        else:
            available_moves.append("#")

    display_grid(available_moves)

    # Validates that the input is an int between 1 and 9 and does not already have a move placed in that spot

    is_valid_user_input = False
    user_input = ""
    move = None
    move_index = None

    while not is_valid_user_input:
        user_input = input("\nPlease enter the number where you would like to place your next move: ")

        try:
            move = int(user_input)
            move_index = move - 1
            if move >= 1 and move <= 9 and GAME_STATE[move_index] == EMPTY:
                is_valid_user_input = True
            else:
                print("\nUser input must be a valid move.")
        except ValueError:
            print("\nUser input must be a valid move.")

    if CURRENT_PLAYER == 1:
        GAME_STATE[move_index] = "X"
    elif CURRENT_PLAYER == 2:
        GAME_STATE[move_index] = "O"

    return move_index

# Returns False if a given move ended the game or if there are no valid moves remaining
# Otherwise it switches the players and returns True
def check_game_ongoing(move_index):
    for winning_line in WINNING_LINES:
        if move_index in winning_line:
            if (GAME_STATE[winning_line[0]] != EMPTY) and (GAME_STATE[winning_line[0]] == GAME_STATE[winning_line[1]] == GAME_STATE[winning_line[2]]):
                display_board()
                if CURRENT_PLAYER == 1:
                    print("\nPlayer One (X) wins!")
                elif CURRENT_PLAYER == 2:
                    print("\nPlayer Two (O) wins!")
                return False

    if EMPTY not in GAME_STATE:
        display_board()
        print("\nPlayer One and Player Two have tied!")
        return False

    switch_current_player()

    return True

# Toggles between Player 1 and Player 2
def switch_current_player():
    global CURRENT_PLAYER

    if CURRENT_PLAYER == 1:
        CURRENT_PLAYER = 2
    elif CURRENT_PLAYER == 2:
        CURRENT_PLAYER = 1

# Runs the game loop
def main():
    start_game()

    is_game_ongoing = True

    while is_game_ongoing:
        display_current_game_state()
        move_index = take_user_move()
        is_game_ongoing = check_game_ongoing(move_index)

if __name__ == "__main__":
    main()
