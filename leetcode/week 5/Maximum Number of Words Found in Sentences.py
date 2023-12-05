# Maximum Number of Words Found in Sentences


class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        tmp = 0

        for sentence in sentences:
            blank = sentence.count(" ")

            # 공백의 개수가 tmp보다 크면 tmp값 최대값으로 갱신
            if tmp < blank:
                tmp = blank

        # 공백의 개수 + 1이 단어의 개수
        return tmp + 1
