# Excel Sheet Column Number


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        answer = 0
        rev_str = columnTitle[::-1]

        for i in range(len(rev_str)):
            answer += (ord(rev_str[i]) - 64) * (26**i)

        return answer


solution = Solution()
solution.titleToNumber("ZY")
