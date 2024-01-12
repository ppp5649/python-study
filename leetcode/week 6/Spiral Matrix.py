# Spiral Matrix

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix[0])
        n = len(matrix)
        answer = []

        while len(answer) != (m*n):
            