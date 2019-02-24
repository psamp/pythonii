# Princess Sampson
# Dr. Lawrence - Python 2
# Tic Tac Toe

import collections

# named tuple type used to model board coordinates
Coordinate = collections.namedtuple("Coordinate", "row slot")

# check the board for a winner
def winner(board):

    # check the rows
    for row in board:
        #delegate to determine if winning row
        if winning_row_col_diag(row):
            return True

    # check the columns
    for col in range(len(board[0])):
        # from each row pull out the appropriate column value
        column = [ 
                board[0][col], 
                board[1][col], 
                board[2][col]
        ]

        # delegate to determine if winning column
        if winning_row_col_diag(column):
            return True
    
    # check the lefhand diagnol
    left_diagnol = [
        board[0][0],
        board[1][1],
        board[2][2]
    ]

    if winning_row_col_diag(left_diagnol):
        return True

    # check the righthand diagnol
    right_diagnol = [
        board[0][2],
        board[1][1],
        board[2][0],
    ]

    if winning_row_col_diag(right_diagnol):
        return True
    
    return False

# determine if this is a winning row, column or diagnol
def winning_row_col_diag(row_col_diag):
        # create a set from list of row, column, or diagnol values
        row_col_diag_set = set(row_col_diag)

        # if there's exactly one element that is not the placeholder in the set
        # then this is a winning row/col/diag
        if ("-" not in row_col_diag_set) and (len(row_col_diag_set) == 1):
            return True
        else:
            return False

# given the board, print its values
def print_board(board):
    
    # print the column numbers
    print("\t1\t2\t3\t")

    # for each row
    for row in range(len(board)):
        # print the row no. plus one and append a tab
        print(row + 1, end="\t")
        # for each slot in a row
        for slot in range(len(board[row])):
            # print the slot's value and append a tab
            print(board[row][slot], end="\t")
        print()

# print the coordinates
def print_coords(coords):

    # for however many coords are left
    for i in range(len(coords)):
        # print the label the player will use to select the coordinate
        print(i + 1, ":", end="\t")
        
        # current coordinate
        current = coords[i]
        
        # print the current coord's row and slot, but 1-indexed for the player
        print("(%d, %d)" % (current.row + 1, current.slot + 1))

# gen a list of coordinates for the player to select from
def coords(board):
    coordinates = []

    # for every row
    for r in range(len(board)):
        # for every slot
        for s in range(len(board[0])):
            # append the current coordinates
            current = Coordinate(row=r, slot=s)
            coordinates.append(current)
    
    return coordinates

# given the board and some coordinates, update the proper slot with the appropriate symbol
def mark(board, selection, turn):
    board[selection.row][selection.slot] = "O" if even(turn) else "X"

# is a number even or odd?
def even(number):
    return number % 2 == 0

# is the input a positive number and in [1, limit)
def valid(input, limit):
    return input.isdigit() and (int(input) in range(1, limit + 1))

def main():

    # initialize the board with blank values
    board = [
        ["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]
    ]

    # turn is odd for Player 1, even for Player 2
    turn = 1

    # generate list of board coordinates
    coordinates = coords(board)

    # play the game until a winner is found
    while not winner(board):

        # name player based on whose turn it is
        player = "Player 2 (O)" if even(turn) else "Player 1 (X)"

        # for saving selection and its validity
        selection = ""
        selection_valid = False

        # prompt the player until valid input is received
        while not selection_valid:

            # print the board
            print_board(board)
            print()

            # ask the user to make a selection
            print("%s select the coordinates where you want to mark the board:" % (player))

            # print the list of coords
            print_coords(coordinates)
            
            # save the user's input
            selection = input()

            # update validity flag with whether a number in the range of the selection labels was entered
            selection_valid = valid(selection, len(coordinates))

        # convert player selected coord label to a num that will not raise an indexing error
        selection = (int(selection) - 1)

        # pull out the actual coords selected
        selectionCoords = coordinates[selection]

        # mark the board in the proper position
        mark(board, selectionCoords, turn)

        # remove the coordinates on this turn from the list of options
        coordinates.pop(selection)

        # increment the turn counter
        turn += 1

    # print the board so players can see who won
    print_board(board)
    print("Game over!")

#call main
main()