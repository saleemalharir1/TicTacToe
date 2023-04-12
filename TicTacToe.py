from art import *
import random

title = text2art("TIC TAC TOE")
board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
player_1 = "X"
player_2 = "O"

def display_board():
    for row in board:
        print("|".join(row))

def check_win(marker):
    for row in board:
        if row.count(marker) == 3:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == marker:
            return True
    if board[0][0] == board[1][1] == board[2][2] == marker:
        return True
    if board[0][2] == board[1][1] == board[2][0] == marker:
        return True
    return False
def play_game():
    # Print the title and the game board
    print(title)
    display_board()
    
    # Start the game loop
    while True:
        # Player 1's turn
        row = int(input("Player 1, choose a row (0-2): "))
        col = int(input("Player 1, choose a column (0-2): "))
        if board[row][col] == " ":
            board[row][col] = player_1
            display_board()
            if check_win(player_1):
                print("Player 1 wins!")
                break
        else:
            print("That space is already taken, try again.")
            continue
        
        # Player 2's turn
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            board[row][col] = player_2
            print("Player 2 chooses row {} column {}".format(row, col))
            display_board()
            if check_win(player_2):
                print("Player 2 wins!")
                break
        else:
            print("That space is already taken, Player 2 chooses again.")
            continue
        
        # Check for a tie
        if all([space != " " for row in board for space in row]):
            print("It's a tie!")
            break

# Start the game
play_game()