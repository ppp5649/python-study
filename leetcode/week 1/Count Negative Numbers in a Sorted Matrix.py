# 1351. Count Negative Numbers in a Sorted Matrix
# 단순히 2중 for문 돌려서 음수 값 탐색 시 ansewr 1씩 증가


# %%
class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        answer = 0

        for m in grid:
            for n in m:
                if n < 0:
                    answer += 1

        return answer


solution = Solution()


# %%
