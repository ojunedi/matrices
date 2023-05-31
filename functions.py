import numpy as np


def norm(X) -> int:
    squared_sum = sum([x ** 2 for x in X])
    return np.sqrt(squared_sum)

def multipy(A: list[list[float]], B: list[list[float]] | list[float]) -> list[list[float]] | list[float]:

    result = [[0]*len(B[0]) for _ in range(len(A))]

    for i in range(len(A)):
    # iterating by column by B
        for j in range(len(B[0])):
            # iterating by rows of B
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]


    return result

def transpose(matrix: list[list[float]]) -> list[list[float]]:
    return [[row[j] for row in matrix] for j in range(matrix[0])]

def getMinorMatrix(matrix, i, j) -> list[list[float]]:
    return [row[:j] + row[j+1:] for row in (matrix[:i]+matrix[i+1:])]

# Calculating the determinant using the laplace expansion
# recursively
# https://en.wikipedia.org/wiki/Laplace_expansion
# REQUIRES: matrix must be an N x N matrix
def getDeterminant(matrix: list[list[float]]) -> float:

    n = len(matrix)
    # base case of 2x2 matrix
    if n == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    # expanding along the first row
    determinant = 0
    for i in range(n):
        determinant +=  ((-1) ** i) * matrix[0][i] * getDeterminant(getMinorMatrix(matrix, 0 , i))
    return determinant


def inverse(matrix: list[list[float]]) -> list[list[float]] | str:
    determinant = getDeterminant(matrix)

    if determinant == 0:
        return "Non-Invertible Matrix!"

    # special case for 2x2 matrix
    if len(matrix) == 2:
        return [[matrix[1][1]/determinant, -1 * matrix[0][1] / determinant], [-1 * matrix[1][0]/determinant, matrix[0][0]/determinant]]

    # find the cofactor matrix
    cofactors = []
    for i in range(len(matrix)):
        coFactorRow = []
        for j in range(len(matrix)):
            minor = getMinorMatrix(matrix, i, j)
            coFactorRow.append((-1)**(i+j) * getDeterminant(minor))
        cofactors.append(coFactorRow)
    
    adjugate = transpose(cofactors)
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            adjugate[r][c] *= (1/determinant)
    
    return adjugate

# using the power iteration 
# copped out and used numpy because implementing it with my own functions was a pain in the ass
def eigenvalues(matrix: list[list[float]], num_iterations: int) -> list[float]:
    x = np.random.rand(len(matrix))
    A = matrix
    lam_prev = 0
    tol = 1e-6
    for _ in range(num_iterations):
        x = A @ x / np.linalg.norm(A @ x)
        lam = (x.T @ A @ x) / (x.T @ x)
        if np.abs(lam - lam_prev) < tol:
            break
        lam_prev = lam

    return list(x), lam

test_matrix = [[2,1],[1,2]]
eigenvector, eigenvalue = eigenvalues(test_matrix, 100)
eigenvalue = round(eigenvalue, 4)
print(eigenvector, eigenvalue)
print(np.dot(test_matrix, eigenvector))

