# # 예외 케이스 2개 나옴 (part 문자열이 여러개 있는경우 다 replace 되어버림)
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            # replace 메소드의 3번째 매개변수에서 몇개 대체할 것인지 정할 수 있음
            # 3번째 매개변수를 비워둔다면 존재하는 모든 부분 문자열을 대체시킴
            s = s.replace(part, "", 1)

        return s


solution = Solution()
print(solution.removeOccurrences("aabababa", "aba"))
