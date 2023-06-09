import pytest
from functions import getDeterminant, inverse, multipy, transpose, getMinorMatrix, eigenvalues
import numpy as np

class TestDeterminant:
    def test_two_by_two(self):
        matrix = [[1, 0], [0, 0]]
        assert getDeterminant(matrix) == 0

        matrix = [[1, 0], [0, 1]]
        assert getDeterminant(matrix) == 1

        matrix = [[1, 7], [6, 9]]
        assert getDeterminant(matrix) == -33

    def test_3x3(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        assert getDeterminant(matrix) == 0

        matrix = [[2,3,7],[1,9,10],[1,8,6]]
        assert getDeterminant(matrix) == -47

        matrix = [[1,1,1],[2,2,2],[1,8,6]]
        assert getDeterminant(matrix) == 0

        matrix = [[0,1,3],[2,4,2],[9,8,11]]
        assert getDeterminant(matrix) == -64


    def test_large_matrix(self):
        matrix = [
            [1, 2, -1, 3, 4, -2, -4],
            [4, 6, 3, 1, 0, -1, 2],
            [2, -4, -2, -1, 2, 3, 1],
            [1, 0, -3, 3, 2, 4, 1],
            [1, 3, -2, 1, 0, 0, 2],
            [1, 3, -2, 3, 5, -2, 1],
            [1, 0, 0, 1, 2, -4, -1]

        ]
        assert getDeterminant(matrix) == -19412


class TestInverse:
    def test_non_invertible_2x2(self):
        matrix = [[0,0],[0,0]]
        assert inverse(matrix) == "Non-Invertible Matrix!"

        matrix = [[1, 0], [0, 0]]
        assert inverse(matrix) == "Non-Invertible Matrix!"

        matrix = [[2, 4], [1, 2]]
        assert inverse(matrix) == "Non-Invertible Matrix!"


    def test_2x2(self):

        matrix = [[1,2],[3,4]]
        assert inverse(matrix) == [[-2, 1], [1.5, -0.5]]

        matrix = [[1, 1], [1, 2]]
        assert inverse(matrix) == [[2, -1], [-1, 1]]

        matrix = [[-3, 2],[1, 4]]
        assert inverse(matrix) == [[-2/7, 1/7], [1/14, 3/14]]

        matrix = [[2, -1], [1, -2]]
        assert inverse(matrix) == [[2/3, -1/3], [1/3, -2/3]]


class TestMultiply:
    def test_2x2_2x2(self):
        identity = [[1,0],[0,1]]

        mat1 = [[1,2],[3,4]]
        assert multipy(identity, mat1) == mat1
        assert multipy(mat1, identity) == mat1

        mat2 = [[0,1],[1,0]]
        assert multipy(identity, mat2) == mat2
        assert multipy(mat2, identity) == mat2

        assert multipy(mat1, mat2) == [[2,1],[4,3]]
        assert multipy(mat2, mat1) == [[3,4],[1,2]]

    def test_2x2_2x1(self):
        identity = [[1,0],[0,1]]
        mat1 = [[1,2],[3,4]]
        mat2 = [[0,1],[1,0]]
        mat3 = [[1,5],[6,9]]
        
        assert multipy(mat1, [[1],[0]]) == [[1],[3]]
        assert multipy(mat2, [[1],[0]]) == [[0],[1]]
        assert multipy(identity, [[6],[9]]) == [[6],[9]]
        assert multipy(mat3, [[2],[1]]) == [[7],[21]]

    def test_1x1_1x1(self):
        assert multipy([[10]], [[7]]) == [[70]]
        assert multipy([[1.5]], [[2]]) == [[3]]
        assert multipy([[9]], [[0.5]]) == [[4.5]]
        assert multipy([[0]], [[12]]) == [[0]]

    def test_3x3_3x1(self):
        identity = [[1,0,0],[0,1,0],[0,0,1]]
        mat1 = [[1,2,3],[4,5,6],[7,8,9]]

        assert multipy(identity, [[1],[2],[3]]) == [[1],[2],[3]]
        assert multipy(mat1, [[0],[1],[0]]) == [[2],[5],[8]]
        assert multipy(mat1, [[2],[1],[3]]) == [[13],[31],[49]]

    def test_3x3_3x3(self):
        identity = [[1,0,0],[0,1,0],[0,0,1]]
        mat1 = [[1,2,3],[4,5,6],[7,8,9]]
        mat2 = [[0,0,0],[0,0,0],[0,0,0]]

        assert multipy(identity, mat1) == mat1
        assert multipy(mat1, mat2) == mat2
        assert multipy(mat1, mat1) == [[30,36,42],[66,81,96],[102,126,150]]

    def test_6x6_6x6(self):
        pass
        #TODO

class TestTranspose:
    def test_2x2(self):
        mat1 = [[1,2],[3,4]]
        identity = [[1,0],[0,1]]
        mat2 = [[0,1],[1,0]]
        assert transpose(mat1) == [[1,3],[2,4]]
        assert transpose(mat2) == mat2
        assert transpose(identity) == identity
    
    def test_3x3(self):
        identity = [[1,0,0],[0,1,0],[0,0,1]]
        assert transpose(identity) == identity
