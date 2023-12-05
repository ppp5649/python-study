# Truncate Sentence


# class Solution:
#     def truncateSentence(self, s: str, k: int) -> str:
#         word_list = s.split()

#         return " ".join(word_list[:k])


class Solution:
    def truncateSentence(self, s, k):
        # 원하는 값의 인덱스를 모두 찾는 방법 (index 함수 쓰면 첫번째만 반환함)
        if len(s.split()) == k:
            return s

        blank_idx = [i for i, el in enumerate(s) if el == " "]
        return s[: blank_idx[k - 1]]


solution = Solution()

print(solution.truncateSentence("Hello how are you Contestant", 4))
