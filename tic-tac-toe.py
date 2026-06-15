CURRENT_PLAYER = 1
GAME_STATE = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

def start_game():
    print("Welcome to Tic Tac Toe!\n")

def display_current_game_state():
    if CURRENT_PLAYER == 1:
        print("It is Player One's (X) turn.\n")
    if CURRENT_PLAYER == 2:
        print("It is Player Two's (O) turn.\n")

    print("Current game board:\n")

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
            if j < i+2:
                row += "|"
        print(row)
        if i < 6:
            print("-----")

    move = input("Please enter the number where you would like to place your next move: ")

def main():
    start_game()
    display_current_game_state()
    take_user_move()

if __name__ == "__main__":
    main()
