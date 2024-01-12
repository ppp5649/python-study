# class Solution:
#     def rotate(arr):
#         l = len(arr)
#         stack = []

#         for i in range(l):
#             for j in range(l, 0, -1):
#                 stack.append(arr[j - 1][i])

#         stack.reverse()
#         new_arr = [[stack.pop() for _ in range(l)] for _ in range(l)]

#         return new_arr


# solution = Solution()
# solution.rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])

# # 기존 index    00 01 02 / 10 11 12 / 20 21 22
# # 회전 후 index 20 10 00 / 21 11 01 / 22 12 02

# # index[0] -> l-1 ~ 0 까지 -1  고정 / l-1 ~ 0 까지 -1  고정 / l-1 ~ 0 까지 -1  고정
# # index[1] -> 0 0 0 / 1 1 1 ... / l-1 까지

# 시행착오 (풀고나서 비효율적인 연산이 있을거라고 예상함)
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# l = len(matrix)
# matrix.reverse()

# for i in range(l):
#     matrix[i].reverse()

# for i in range(l):
#     for j in range(l):
#         matrix[j].insert(0, matrix[i].pop())

# for i in range(l):
#     matrix[i].reverse()


# 최종
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        l = len(matrix)

        for m in range(l - 1, 0, -1):
            for n in range(l - 1, 0, -1):
                matrix[m].insert(0, matrix[n].pop())

        return matrix


solution = Solution()
print(solution.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
