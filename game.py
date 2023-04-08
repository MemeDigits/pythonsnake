import random

# Function to print the board
def print_board(board):
    print('-------------')
    print('| ' + str(board[0]) + ' | ' + str(board[1]) + ' | ' + str(board[2]) + ' |')
    print('-------------')
    print('| ' + str(board[3]) + ' | ' + str(board[4]) + ' | ' + str(board[5]) + ' |')
    print('-------------')
    print('| ' + str(board[6]) + ' | ' + str(board[7]) + ' | ' + str(board[8]) + ' |')
    print('-------------')

# Function to check if someone has won
def check_win(board, player):
    # Check for horizontal wins
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player):
        return True
    # Check for vertical wins
    elif (board[0] == player and board[3] == player and board[6] == player) or \
         (board[1] == player and board[4] == player and board[7] == player) or \
         (board[2] == player and board[5] == player and board[8] == player):
        return True
    # Check for diagonal wins
    elif (board[0] == player and board[4] == player and board[8] == player) or \
         (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False

# Function to play the game
def play_game():
    # Set up the board
    board = [1, 2, 3,
