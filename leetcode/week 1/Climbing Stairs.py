# 70. Climbing Stairs
# 가짓 수를 수열처럼 나열해보니 우연히 피보나치 수열과 같은 것을 발견


# %%
class Solution:
    def climbStairs(self, n: int) -> int:
        answer = [1, 2]

        if n == 1 or n == 2:
            return n

        while True:
            answer.append(answer[-1] + answer[-2])

            if len(answer) == n:
                break

        return answer[-1]


solution = Solution()
solution.climbStairs(5)

# %%
