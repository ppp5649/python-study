# 사칙연산 계산기
# 풀이 시간 : 10분


class Calculator:
    def __init__(self, nums):
        self.nums = nums

    def sum(self):
        return sum(self.nums)

    def avg(self):
        return sum(self.nums) / len(self.nums)


cal1 = Calculator([1, 2, 3, 4, 5])

print(cal1.sum())
print(cal1.avg())
