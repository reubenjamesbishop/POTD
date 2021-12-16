from pieces import *
import copy
import time
import sys
from multiprocessing import Pool, Process, Event, Manager
from Utilities import IslandFinder
from datetime import date

count = 0
solution_found = False
island_finder = None


def oob_valid(piece, row, column):
    """Determines whether piece at given position is out of bounds and returns bool"""
    bottom_boundary = 6-row
    right_boundary = 6-column
    height = len(piece)-1
    width = len(piece[0])-1

    if (height > bottom_boundary) or (width > right_boundary):
        return False
    return True


def init_board(date_array):
    """Initialise an empty board with no pieces."""

    month = date_array[0]
    day = date_array[1]

    board = [
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1],
    ]

    tempday, tempmonth = day, month
    day_row, month_row = 0, 0

    if month not in range(1, 13) or day not in range(1, 32):
        print('Invalid Date Input')
    else:
        while tempday > 7:
            tempday -= 7
            day_row += 1

        while tempmonth > 6:
            tempmonth -= 6
            month_row += 1

        board[month_row][month-1-(month_row*6)] = '1'
        board[day_row+2][day-1-(day_row*7)] = '1'

    return board


def print_board(board):
    """Pretty print current board"""
    s = [[str(e) for e in row] for row in board]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))


def convolute(board, piece, row, column):
    """ Function to convolve an oriented piece in a specific coordinate return if valid."""
    temp_board = copy.deepcopy(board)
    try:
        count_x, count_y = 0, 0
        for board_row in range(row, row+len(piece)):
            count_x = 0
            count_y += 1
            for board_column in range(column, column+len(piece[0])):
                count_x += 1
                if(board[board_row][board_column] == 0 or not piece[count_y-1][count_x-1]):
                    if(piece[count_y-1][count_x-1]):
                        temp_board[board_row][board_column] = piece[count_y-1][count_x-1]
                else:
                    temp_board = board.copy()
                    print(1/0)
    except IndexError:
        # logging.info('Invalid placement of piece... (out of bounds)')
        return None
    except ZeroDivisionError:
        # print('Tried to place piece on unavailable slot...')
        return None
    # print('Everything worked! Returning an updated board..............')
    return temp_board


def get_next_layer(board, layer):
    if is_solved(board):
        return None
    layer_key = layer[0][0][0]
    if(layer_key == 'H'):
        return pieces_dict['A']
    else:
        return pieces_dict[chr(ord(layer_key)+1)]


def illegal_move(coord, layer, index):
    if index in layer[1]:
        if coord in layer[1][index]:
            return True


def board_invalid(board):
    island_finder = IslandFinder(board)
    if island_finder.get_min_island_size() < 5:
        return True


def can_convolute(board_cell, piece_cell):
    if board_cell == 0 or not piece_cell:
        return True
    else:
        return False


def is_solved(board):
    for row in board:
        if(0 in row):
            return False
    return True


def add_layer(board, layer, quit=None, return_value=None):
    global count

    if is_solved(board):
        # print_board(board)
        with open('log.txt', 'a') as f:
            f.write(
                f"FINISHED! Solution found. No. iterations: {count}")
        print('---------------------------------------------------\n')
        print(
            f'FINISHED! Solution found. No. iterations: {count}\n')
        print('---------------------------------------------------\n')
        if quit:
            return_value[0] = board
            quit.set()
        return board

    if board_invalid(board):
        return None

    for col in range(0, 7):
        for row in range(0, 7):
            for orientation_index, oriented_piece in enumerate(layer[0]):
                # if illegal_move(tuple([col, row]), layer, orientation_index):
                #     continue
                new_board = None
                if(can_convolute(board[row][col], oriented_piece[0][0]) and oob_valid(oriented_piece, row, col)):
                    new_board = convolute(
                        board, oriented_piece, row, col)
                if new_board:
                    count += 1
                    if count % 500 == 0:
                        print(f'Current iteration: {count}')
                        # print_board(board)
                    next_layer = get_next_layer(new_board, layer[0])
                    temp = add_layer(new_board, next_layer,
                                     quit, return_value)
                    if not temp:
                        continue
                    else:
                        return temp


def single_solve_puzzle(board):
    return add_layer(board, pieces_dict['A'])


def parallel_solve_puzzle(board):
    manager = Manager()
    return_value = manager.dict()
    quit = Event()
    pool = []
    char = 'A'

    for _ in range(8):
        pool.append(Process(target=add_layer, args=(
            board, pieces_dict[char], quit, return_value,)))
        char = chr(ord(char)+1)
    [p.start() for p in pool]

    start_time = time.time()
    quit.wait()
    with open('log.txt', 'a') as f:
        f.write(f". Runtime: {(time.time() - start_time)} seconds.\n")

    [p.terminate() for p in pool]
    [p.join() for p in pool]
    return return_value[0]


def main():
    # print command line arguments
    if len(sys.argv) > 1:
        board = init_board([int(sys.argv[1]), int(sys.argv[2])])
    else:
        todays_date = date.today()
        board = init_board([todays_date.month, todays_date.day])
        # board = init_board([6, 20])

    start_time = time.time()
    solved = parallel_solve_puzzle(board)
    # solved = single_solve_puzzle(board)
    print_board(solved)
    print("\n------------ %s seconds ------------" %
          (time.time() - start_time))


if __name__ == "__main__":
    main()
