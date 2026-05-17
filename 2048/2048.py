# COMMENT STRUCTURE
# ? is func desc
# ! describes what is happening
# ^ is what is returned

import numpy as np
import pandas as pd
import random
import os

def new_board(size=4):                                                  #?takes the size variable and creates the board with size 4x4
    board = np.zeros((size, size), dtype=int)                           #!makes the board 4x4 with all zeros for now
    board = add_random_tile(board)                                      #!adds the first random tile
    board = add_random_tile(board)                                      #!adds the second random tile
    return board                                                        #^returns initialized board

def add_random_tile(board):                                             #? takes the current board as input
    empty_cells = [tuple(cell) for cell in np.argwhere(board == 0)]     #! find all empty cells as (row, col) pairs
    if not empty_cells:                                                 #! if there are no empty cells left, do nothing
        return board
    r, c = random.choice(empty_cells)                                   #! randomly pick one empty cell’s coordinates
    board[r, c] = 4 if random.random() < 0.1 else 2                     #! place a '4' (10% chance) or a '2' (90% chance)
    return board                                                        #^ return the updated board



def compress_and_merge(row):                                            #?handles merging logic for a single row
    nonzero = row[row != 0]                                             #!removes zeros
    merged = []
    score_gain = 0
    i = 0
    while i < len(nonzero):                                             #!go through each tile
        if i + 1 < len(nonzero) and nonzero[i] == nonzero[i + 1]:
            merged.append(nonzero[i] * 2)                               #!merge equal tiles
            score_gain += nonzero[i] * 2
            i += 2
        else:
            merged.append(nonzero[i])
            i += 1
    merged += [0] * (len(row) - len(merged))                            #!pad with zeros on the right
    return np.array(merged), score_gain                                 #^returns new row and score gained


def move_left(board):                                                   #?handles movement to the left
    new_board = np.zeros_like(board)
    total_gain = 0
    moved = False

    for i in range(board.shape[0]):                                     #!process each row
        new_row, gain = compress_and_merge(board[i])
        if not np.array_equal(new_row, board[i]):                       #!check if row changed
            moved = True
        new_board[i] = new_row
        total_gain += gain
    return new_board, moved, total_gain                                 #^returns new board, whether moved, and gained score


def move_right(board):                                                  #?handles movement to the right
    flipped = np.fliplr(board)                                          #!flip left-right
    new_flipped, moved, gain = move_left(flipped)                       #!reuse move_left logic
    return np.fliplr(new_flipped), moved, gain                          #^returns flipped-back board


def move_up(board):                                                     #?handles upward movement
    transposed = board.T                                                #!transpose converts columns to rows
    new_t, moved, gain = move_left(transposed)                          #!reuse move_left on transposed board
    return new_t.T, moved, gain                                         #^returns transposed-back board


def move_down(board):                                                   #?handles downward movement
    transposed = board.T                                                #!transpose for column-based movement
    new_t, moved, gain = move_right(transposed)                         #!reuse move_right on transposed board
    return new_t.T, moved, gain                                         #^returns board back to normal


def can_move(board):                                                    #?checks if any valid move is left
    if 0 in board:                                                      #!if there’s an empty cell, move possible
        return True
    for r in range(board.shape[0]):                                     #!check adjacent equal tiles horizontally & vertically
        for c in range(board.shape[1]):
            if r + 1 < board.shape[0] and board[r, c] == board[r + 1, c]:
                return True
            if c + 1 < board.shape[1] and board[r, c] == board[r, c + 1]:
                return True
    return False                                                        #^returns True if move possible else False


def has_won(board, target=2048):                                        #?checks if player reached target tile (2048)
    return np.any(board >= target)                                      #^returns True if 2048 or higher is present


def print_board(board, score, highscore):                               #?prints the game board and info
    os.system('cls' if os.name == 'nt' else 'clear')                    #!clear console before printing
    df = pd.DataFrame(board)                                            #!convert board to DataFrame for a nice gridlike print
    print("\n2048 Python Edition\n")                
    print(df.replace(0, '.'))                                           #!replace zeros with dots for clarity
    print(f"\nScore: {score} | Highscore: {highscore}")                 #!displays the scores
    print("Controls: W/A/S/D = move | R = restart | Q = quit\n")        #!controls info 
                                                                        #!(W for up, A for left, S for down and D for right)


def play_game():                                                        #? main function controlling the game loop
    board = new_board()
    score = 0
    highscore = 0

    while True:
        print_board(board, score, highscore)

        if has_won(board):                                              #! check if reached 2048
            print(f"\n You reached 2048! Final Score: {score}")
            break

        if not can_move(board):                                         #! check if no moves left
            print("\n Game Over!")
            break

        move = input("Move: ").lower().strip()                          #! take player input

        if move == 'q':
            print("\n You quit the game.")
            break
        if move == 'r':
            print("\n Restarting...")
            board = new_board()
            score = 0
            continue

        if move == 'a':
            updated_board, moved, gain = move_left(board)
        elif move == 'd':
            updated_board, moved, gain = move_right(board)
        elif move == 'w':
            updated_board, moved, gain = move_up(board)
        elif move == 's':
            updated_board, moved, gain = move_down(board)
        else:
            continue                                                    # invalid input, ignore

        if moved:                                                       #! only add new tile if board changed
            board = add_random_tile(updated_board)
            score += gain
            highscore = max(highscore, score)


# ---------- Start the Game ----------
play_game()
