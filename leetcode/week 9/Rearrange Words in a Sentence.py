class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text[0].lower() + text[1:]
        words = text.split(" ")
        words.sort(key=len)
        ordered_text = " ".join(words)

        return ordered_text[0].upper() + ordered_text[1:]
