import pytest
from functions import getDeterminant, inverse

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