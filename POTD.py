from multiprocessing.queues import Queue
from pieces import *
import copy
import time
import sys
from multiprocessing import Process, Event, Queue
from Utilities import IslandFinder

count = 0
solution_found = False


def classic_init_board():
    """Initialise an empty board with no pieces."""
    # TODO: write a function for the init board
    return [
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1],
    ]


def cli():
    """Function which allows for command line interface when inputting dates"""

    while True:
        month = int(input("Please enter month:"))
        if month not in range(1, 13):
            print('Invalid Month input')
            continue
        break

    while True:
        day = int(input("Please enter day:"))
        if day not in range(1, 32):
            print('Invalid day input')
            continue
        break
    return month, day


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


def check_surrounds(board, row, column):
    """
    Function to check the surrounding coordinates on a board.
    Returns False if current thing is an invalid board.
    """

    current = board[row][column]

    if current != 0:
        return True

    try:
        up = board[row-1][column]
        down = board[row+1][column]
        left = board[row][column-1]
        right = board[row][column+1]

    except IndexError:
        # print('CANT CHECK OUT OF BOUNDS!')
        return True

    # If there are no empty spaces around the current empty spot, invalid board (return false)
    if(up != 0 and down != 0 and left != 0 and right != 0):
        return False
    else:
        return True


def check_board_state(board):
    """
    Function to check surrounds of every piece on board.
    Returns False if board state is invalid.
    """

    for row in range(0, 7):
        for column in range(0, 7):
            is_valid = check_surrounds(board, row, column)
            if not is_valid:
                return False
    return True


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
    except IndexError as e:
        # logging.info('Invalid placement of piece... (out of bounds)')
        return None
    except ZeroDivisionError as e:
        # print('Tried to place piece on unavailable slot...')
        return None
    # print('Everything worked! Returning an updated board..............')
    return temp_board


def get_next_layer(board, layer):

    global count
    solved = True

    for row in board:
        if(0 in row):
            solved = False
    if solved:
        with open('log.txt', 'a') as f:
            f.write(
                f"FINISHED! Solution found for date {sys.argv[2]}/{sys.argv[1]}. No. iterations: {count}")
        print(
            f'FINISHED! Solution found for date {sys.argv[2]}/{sys.argv[1]}. No. iterations: {count}')
        print('-----------------------------')

        return None

    layer_key = layer[0][0][0]
    if(layer_key == 'A'):
        return pieces_dict['B']
    if(layer_key == 'B'):
        return pieces_dict['C']
    if(layer_key == 'C'):
        return pieces_dict['D']
    if(layer_key == 'D'):
        return pieces_dict['E']
    if(layer_key == 'E'):
        return pieces_dict['F']
    if(layer_key == 'F'):
        return pieces_dict['G']
    if(layer_key == 'G'):
        return pieces_dict['H']
    if(layer_key == 'H'):
        return pieces_dict['A']


def add_layer(board, layer, found_event=None, Q=None):
    global count
    global skipped

    IF = IslandFinder(board)
    if IF.get_min_island_size() < 5:
        return False

    for col in range(0, 7):
        for row in range(0, 7):
            for orientation_index, oriented_piece in enumerate(layer[0]):
                leave = False
                if orientation_index in layer[1]:
                    if tuple([col, row]) in layer[1][orientation_index]:
                        leave = True
                if leave:
                    continue
                new_board = None
                if((board[row][col] == 0 or not oriented_piece[0][0]) and oob_valid(oriented_piece, row, col)):
                    new_board = convolute(
                        board, oriented_piece, row, col)
                if new_board:
                    count += 1
                    if count % 500 == 0:
                        print(f'Current iteration: {count}')
                        # print_board(new_board)
                        # print('-----------------------------')

                    next_layer = get_next_layer(new_board, layer[0])
                    if next_layer:
                        temp = add_layer(new_board, next_layer, found_event)
                        if not temp:
                            continue
                    else:
                        print_board(new_board)
                        if found_event:
                            found_event.set()
                        return new_board
    return False


def single_solve_puzzle(board):
    start_time = time.time()
    add_layer(board, pieces_dict['A'])
    print("--- %s seconds ---" % (time.time() - start_time))
    # return None


def parallel_solve_puzzle(board):
    found_event = Event()
    # Q = Queue()
    pA = Process(target=add_layer, args=(
        board, pieces_dict['A'], found_event,))
    pB = Process(target=add_layer, args=(
        board, pieces_dict['B'], found_event,))
    pC = Process(target=add_layer, args=(
        board, pieces_dict['C'], found_event,))
    pD = Process(target=add_layer, args=(
        board, pieces_dict['D'], found_event,))
    pE = Process(target=add_layer, args=(
        board, pieces_dict['E'], found_event,))
    pF = Process(target=add_layer, args=(
        board, pieces_dict['F'], found_event,))
    pG = Process(target=add_layer, args=(
        board, pieces_dict['G'], found_event,))
    pH = Process(target=add_layer, args=(
        board, pieces_dict['H'], found_event,))

    pool = [pA, pB, pC, pD, pE, pF, pG, pH]
    [p.start() for p in pool]

    start_time = time.time()
    found_event.wait()
    print("--- %s seconds ---" % (time.time() - start_time))
    with open('log.txt', 'a') as f:
        f.write(f". Runtime: {(time.time() - start_time)} seconds.\n")

    [p.terminate() for p in pool]
    [p.join() for p in pool]

    # y = [x for x in Q]
    # print(y)

    # while(True):
    #     # print('STARTED WHILE LOOP')

    #     running = [p.is_alive() for p in processes]

    #     for p in running:
    #         # print(f'CHECKING IF {p} IS RUNNING...')
    #         if not p:
    #             idx = running.index(p)
    #             # print(f'Process {idx} has terminated!')
    #             processes.pop(idx)
    #             [x.terminate() for x in processes]
    #             # print('KILLED PROCESSES, RETUNING FROM PARALLEL SOLVE')
    #             print("--- %s seconds ---" % (time.time() - startTimes[idx]))
    #             return None


def main():
    # print command line arguments
    board = init_board([int(sys.argv[1]), int(sys.argv[2])])
    parallel_solve_puzzle(board)
    # single_solve_puzzle(board)

    # print_board(solved_board)


if __name__ == "__main__":
    main()
