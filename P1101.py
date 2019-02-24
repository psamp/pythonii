# Princess Sampson

def main():
    size = int(input('Please enter grid size: '))

    grid = []

    # create size length rows
    for row in range(size):
        grid.append([0] * size)

    # Problem 1
    # for row in range(size):
    #     for column in range(size):
    #         grid[row][column] = column
    
    # Problem 2
    # for row in range(size):
    #     for column in range(size):
    #         grid[row][column] = row

    # Problem 3
    # for row in range(size):
    #     for column in range(size):
    #         grid[row][column] = ((row + 1) * 5) - column

    # Problem 4
    for row in range((size - 1), -1, -1):
        print("row:", row)
        for column in range(size):
            grid[row][column] = ((row + 1) * 5) - column

    
    print_grid(grid)

# print nested list as a grid
def print_grid(grid):
    for row in grid:
        print(row)

# call main
main()