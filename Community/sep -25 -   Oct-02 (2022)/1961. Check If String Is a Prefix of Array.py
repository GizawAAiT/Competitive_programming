class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        while words and s:
            if len(s) >= len(words[0]) and s[:len(words[0])]!=words[0]:
                return False
            elif len(s) >= len(words[0]) :
                s = s[len(words[0]):]
                words.pop(0)
            else: return False
        return not s
                