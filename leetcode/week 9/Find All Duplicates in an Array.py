# from collections import Counter


# class Solution:
#     def findDuplicates(self, nums: list[int]) -> list[int]:
#         counter = Counter(nums)
#         twice = []

#         for k, v in counter.items():
#             if v == 2:
#                 twice.append(k)

#         return twice


# solution = Solution()
# print(solution.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))


class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        nums.sort()
        twice = []
        print(nums)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                twice.append(nums[i])

        return twice


solution = Solution()
print(solution.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
