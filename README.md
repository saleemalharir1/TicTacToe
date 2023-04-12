# Tic Tac Toe

This is a simple command line version of the classic game Tic Tac Toe, written in Python. The game board is represented by a 3x3 grid of cells, and players take turns placing their markers (X or O) on the board until one player wins or the game ends in a tie.

## Requirements

This game requires Python 3.x and the `art` module to be installed. You can install `art` using pip:
'''
pip install art
'''

## How to Play

To start the game, run the `play_game()` function in the command line. The game will display a 3x3 grid with empty cells represented by blank spaces. Player 1 will be X and Player 2 will be O.

On their turn, players will be prompted to choose a row and column to place their marker. Players must input numbers between 0 and 2 to choose a valid cell. If the chosen cell is already taken, the player will be prompted to choose again.

The game will continue until one player wins by placing their markers in a row, column, or diagonal, or until the game board is filled with markers and no more moves are possible, resulting in a tie.

## Code Explanation

The game logic is defined by several functions, including `display_board()` which prints the current state of the game board, and `check_win(marker)` which checks if a player has won by placing their markers in a row, column, or diagonal.

The `play_game()` function is the main game loop that prompts players to take turns and updates the game board until a winner is determined or the game ends in a tie. The game uses the `random` module to simulate the moves of Player 2.

Enjoy the game!
