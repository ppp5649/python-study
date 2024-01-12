class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        powers = []

        # power 계산해서 list에 순서대로 넣음
        for i in range(lo, hi + 1):
            power = 0
            while i != 1:
                i = i / 2 if i % 2 == 0 else 3 * i + 1
                power += 1
            powers.append(power)

        # lo ~ hi에 해당하는 숫자와 power값을 tuple로 묶은 다음 list로 만듬
        # enumerate의 index가 붙는 특성과 start 매개변수를 활용
        powers_tup = [i for i in enumerate(powers, start=lo)]

        # key 매개변수에 lambda 함수를 이용하여 tuple의 2번째 요소 기준으로 sort (오름차순)
        sorted_by_power = sorted(powers_tup, key=lambda x: x[1])

        return sorted_by_power[k - 1][0]


solution = Solution()
print(solution.getKth(7, 11, 4))
