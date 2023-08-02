# Pascal's Triangle


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # 길이가 i + 1인 1로만 구성된 2차원 배열
        # 예를 들어, numRows가 5라면 길이가 1, 2, 3, 4, 5인 배열이라고 생각하면 됨
        # ex) [1] / [1,1] / [1,1,1] / [1,1,1,1] / [1,1,1,1,1]
        triangle = [[1] * (i + 1) for i in range(numRows)]

        ### row와 col의 range 설정 ###
        # row(행) : 2부터 numRows-1 까지 바뀌어야 하는 행이므로 range를 2부터 numRows까지 설정
        # col(열) : 0과 마지막 열을 제외한 나머지가 바뀌어야 하는 열이므로 range를 1부터 row까지 설정
        # 값 재선언 : row행의 col열의 값은 (row-1)행의 (col-1)열의 값 + (row-1)행의 col열의 값
        for row in range(2, numRows):
            for col in range(1, row):
                triangle[row][col] = triangle[row - 1][col - 1] + triangle[row - 1][col]

        return triangle


solution = Solution()

print(solution.generate(7))


# 길이가 1개씩 늘어나는 리스트 만드는 사고 과정

# for i in range(5):
#     for j in range(i + 1):
#         print(j, j + 1)
#     print("\n")
