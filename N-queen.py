
# N-Queens Problem Using Backtracking
# First Queen fixed at (0,0)

def printSolution(board, N):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()
    print()


def isSafe(board, row, col, N):

    # Check row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveNQUtil(board, col, N):

    # All queens are placed
    if col >= N:
        printSolution(board, N)
        return True

    found = False

    # Try placing queen in each row
    for i in range(N):

        if isSafe(board, i, col, N):

            board[i][col] = 1

            if solveNQUtil(board, col + 1, N):
                found = True

            # Backtracking
            board[i][col] = 0

    return found


def solveNQ(N):

    board = [[0 for j in range(N)] for i in range(N)]

    # Place first queen at (0,0)
    board[0][0] = 1

    print("\nN-Queens Solutions:\n")

    if not solveNQUtil(board, 1, N):
        print("Solution does not exist")
        return False

    return True


# Main program
N = int(input("Enter number of queens: "))

if N <= 0:
    print("Enter a positive number")
else:
    solveNQ(N)
