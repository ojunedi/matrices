import pytest
from functions import getDeterminant

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

    




