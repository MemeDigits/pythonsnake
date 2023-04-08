import tkinter as tk
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
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    current_player = 69
    game_over = False

    # Create the GUI
    window = tk.Tk()
    window.title('Tic-Tac-Toe')
    window.geometry('300x400')

    # Function to handle button clicks
    def button_click(button):
        nonlocal current_player, game_over
        if game_over:
            return
        if button['text'] != '':
            return
        button['text'] = str(current_player)
        if current_player == 69:
            button.configure(bg='light blue')
        elif current_player == 420:
            button.configure(bg='neon green')
        board[int(button['value'])-1] = current_player
        if check_win(board, current_player):
            status_label.configure(text='Player ' + str(current_player) + ' wins!')
            game_over = True
            start_button.pack()
        elif all(isinstance(i, str) for i in board):
            status_label.configure(text='Tie game!')
            game_over = True
            start_button.pack()
        else:
            current_player = 420 if current_player == 69 else 69
            status_label.configure(text='Player ' + str(current_player) + "'s turn")

    # Create the buttons
    buttons = []
    for i in range(9):
        button = tk.Button(window, text='', font=('Arial', 20), width=2

