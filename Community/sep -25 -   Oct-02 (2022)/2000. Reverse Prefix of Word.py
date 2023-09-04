class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ind = word.index(ch)+1  if ch in set(word) else -1
        return word if ind == -1 else "".join(list(reversed(list(word[:ind])))) + word[ind:] 