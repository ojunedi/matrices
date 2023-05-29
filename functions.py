def transpose(matrix: list[list[int]]) -> list[list[int]]:
    return [[row[j] for row in matrix] for j in range(matrix[0])]

def getMinor(matrix, i, j):
    return [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]

# Calculating the determinant using the laplace expansion
# recursively
# https://en.wikipedia.org/wiki/Laplace_expansion
# REQUIRES: matrix must be an N x N matrix
def getDeterminant(matrix: list[list[int]]) -> int:

    n = len(matrix)
    # base case of 2x2 matrix
    if n == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    # expanding along the first row
    determinant = 0
    for i in range(n):
        determinant +=  ((-1) ** i) * matrix[0][i] * getDeterminant(getMinor(matrix, 0 , i))
    return determinant


def eigenvalues():
    pass

def inverse(matrix: list[list[int]]):
    pass


# this is very weird