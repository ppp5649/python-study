# 조건 1) 알파벳은 모두 뒤집는다
# 조건 2) 알파벳을 제외한 문자는 위치가 바뀌면 안된다


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        rvs_s = s[::-1]
        result = ""

        # 뒤집어진 str을 알파벳 빼고 모두 제거
        for c in rvs_s:
            if c.isalpha() == False:
                rvs_s = rvs_s.replace(c, "")

        for idx in range(len(s)):
            # 알파벳인 경우 result 문자열에 추가
            # 문자를 추가한 후에는 맨 앞의 문자는 삭제 후 재선언
            if s[idx].isalpha() == True:
                result += rvs_s[0]
                rvs_s = rvs_s[1:]
            # 알파벳이 아닌 경우 그대로 더함(idx가 변하면 안되기 때문에)
            else:
                result += s[idx]

        return result


solution = Solution()
print(solution.reverseOnlyLetters("7_28]"))
