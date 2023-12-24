def isSafe(mat, r, c):
    for i in range(r):
        if mat[i][c] == 'Q':
            return False

    (i, j) = (r, c)
    while i >= 0 and j >= 0:
        if mat[i][j] == 'Q':
            return False
        i = i - 1
        j = j - 1

    (i, j) = (r, c)
    while i >= 0 and j < len(mat):
        if mat[i][j] == 'Q':
            return False
        i = i - 1
        j = j + 1

    return True

def printSolution(mat, solutions):
    solution_copy = [list(row) for row in mat]
    solutions.append(solution_copy)

def nQueen(mat, r, solutions):
    if r == len(mat):
        printSolution(mat, solutions)
        return

    for i in range(len(mat)):
        if isSafe(mat, r, i):
            mat[r][i] = 'Q'
            nQueen(mat, r + 1, solutions)
            mat[r][i] = '-'

N = 8
mat = [['-' for x in range(N)] for y in range(N)]
solutions = []

nQueen(mat, 0, solutions)

# Print all solutions
for idx, solution in enumerate(solutions):
    print(f"Solution {idx + 1}:")
    for row in solution:
        print(' '.join(row))
    print()
