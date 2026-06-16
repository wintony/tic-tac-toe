CURRENT_PLAYER = 1
GAME_STATE = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
WINNING_MOVES = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def start_game():
    print("Welcome to Tic Tac Toe!")

def display_board():
    print("\nCurrent game board:\n")

    for i in range(0, 9, 3):
        row = ""
        for j in range(i, i+3):
            if GAME_STATE[j] == " ":
                row += " "
            else:
                row += GAME_STATE[j]
            if j < i+2:
                row += "|"
        print(row)
        if i < 6:
            print("-----")

def display_current_game_state():
    if CURRENT_PLAYER == 1:
        print("\nIt is Player One's (X) turn.")
    elif CURRENT_PLAYER == 2:
        print("\nIt is Player Two's (O) turn.")

    display_board()

def take_user_move():
    print("\nAvailable moves are shown below:\n")

    for i in range(0, 9, 3):
        row = ""
        for j in range(i, i+3):
            if GAME_STATE[j] == " ":
                row += str(j+1)
            else:
                row += "#"
            if j < i+2:
                row += "|"
        print(row)
        if i < 6:
            print("-----")

    is_valid_user_input = False
    user_input = ""
    move = None

    while not is_valid_user_input:
        user_input = input("\nPlease enter the number where you would like to place your next move: ")

        try:
            move = int(user_input)
            if move >= 1 and move <= 9 and GAME_STATE[move-1] == " ":
                is_valid_user_input = True
            else:
                print("User input must be a valid move.")
        except ValueError:
            print("User input must be a valid move.")

    if CURRENT_PLAYER == 1:
        GAME_STATE[move-1] = "X"
    elif CURRENT_PLAYER == 2:
        GAME_STATE[move-1] = "O"

    return move

def check_game_ongoing(move):
    for winning_move in WINNING_MOVES:
        if move in winning_move:
            if (GAME_STATE[winning_move[0]] != " ") and (GAME_STATE[winning_move[0]] == GAME_STATE[winning_move[1]] == GAME_STATE[winning_move[2]]):
                display_board()
                if CURRENT_PLAYER == 1:
                    print("\nPlayer One (X) wins!")
                elif CURRENT_PLAYER == 2:
                    print("\nPlayer Two (O) wins!")
                return False

    if " " not in GAME_STATE:
        display_board()
        print("\nPlayer One and Player Two have tied!")
        return False

    return True

def switch_current_player():
    global CURRENT_PLAYER

    if CURRENT_PLAYER == 1:
        CURRENT_PLAYER = 2
    elif CURRENT_PLAYER == 2:
        CURRENT_PLAYER = 1

def main():
    start_game()

    is_game_ongoing = True

    while is_game_ongoing:
        display_current_game_state()
        move = take_user_move() - 1
        is_game_ongoing = check_game_ongoing(move)

        switch_current_player()

if __name__ == "__main__":
    main()
