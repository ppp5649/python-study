# Two Sum
# from itertools import combinations


# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         nC2 = list(combinations(nums, 2))
#         indexes = list(combinations(range(len(nums)), 2))
#         sum_c = list(map(sum, nC2))

#         t_idx = sum_c.index(target)

#         return list(indexes[t_idx])


# solution = Solution()
# print(solution.twoSum([2, 7, 11, 15], 9))

# 리스트 컴프리헨션은 왼쪽에서 오른쪽으로 실행된다. 그러므로 2중 for문을 사용할 땐 바깥쪽 for문이 왼쪽에 가야한다.

# ### 예시 ###
# num = 4

# # 2중 for문
# arr = []
# for i in range(num - 1):
#     for j in range(i + 1, num):
#         arr.append((i, j))

# # 리스트 컴프리헨션
# arr = [(i, j) for i in range(num - 1) for j in range(i + 1, num)]
# print(arr)

# # combinations의 index 구하기 -> range 이용

# indexes = list(combinations(range(4), 2))
# print(indexes)


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
