CURRENT_PLAYER = 1
GAME_STATE = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
WINNING_MOVES = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def start_game():
    print("Welcome to Tic Tac Toe!\n")

def display_current_game_state():
    if CURRENT_PLAYER == 1:
        print("It is Player One's (X) turn.\n")
    elif CURRENT_PLAYER == 2:
        print("It is Player Two's (O) turn.\n")

    print("Current game board:\n")

    # TODO: Use range to condense the below logic
    print(f"{GAME_STATE[0]}|{GAME_STATE[1]}|{GAME_STATE[2]}")
    print("-----")
    print(f"{GAME_STATE[3]}|{GAME_STATE[4]}|{GAME_STATE[5]}")
    print("-----")
    print(f"{GAME_STATE[6]}|{GAME_STATE[7]}|{GAME_STATE[8]}\n")

def take_user_move():
    print("Available moves are shown below:\n")

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

    # TODO: Validate input is a valid move int
    move = int(input("Please enter the number where you would like to place your next move: "))

    if CURRENT_PLAYER == 1:
        GAME_STATE[move-1] = "X"
    elif CURRENT_PLAYER == 2:
        GAME_STATE[move-1] = "O"

def check_game_ongoing():
    # Check if any moves are still available
    # TODO: Keep track of user moves. If move == 9, return True
    move_available = False

    for i in range(9):
        if GAME_STATE[i] == " ":
            move_available = True

    if not move_available:
        print("Player One and Player Two have tied!")
        return False

    # TODO: only check winning moves containing the most recent user input move
    for winning_move in WINNING_MOVES:
        # TODO: Improve logic check to make sure "winning move" is not 3-in-a-row of blank spaces
        if (GAME_STATE[winning_move[0]] == GAME_STATE[winning_move[1]] == GAME_STATE[winning_move[2]]) and (GAME_STATE[winning_move[0]] != " "):
            if CURRENT_PLAYER == 1:
                print("Player One (X) wins!")
            elif CURRENT_PLAYER == 2:
                print("Player Two (O) wins!")
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
        take_user_move()
        is_game_ongoing = check_game_ongoing()

        switch_current_player()

if __name__ == "__main__":
    main()
