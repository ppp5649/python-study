# Largest Local Values in a Matrix


class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        stack = []
        answer = []

        for i in range(1, n - 1):
            for j in range(1, n - 1):
                stack.append(grid[i - 1][j - 1])
                stack.append(grid[i - 1][j])
                stack.append(grid[i - 1][j + 1])
                stack.append(grid[i][j - 1])
                stack.append(grid[i][j])
                stack.append(grid[i][j + 1])
                stack.append(grid[i + 1][j - 1])
                stack.append(grid[i + 1][j])
                stack.append(grid[i + 1][j + 1])
                answer.append(max(stack))
                stack.clear()

        result = [[] for i in range(n - 2)]

        for i in range(n - 2):
            result[i].append(answer[i * (n - 2)])
            result[i].append(answer[(i + 1) * (n - 2)])
            result[i].append(answer[(i + 2) * (n - 2)])

        return result
