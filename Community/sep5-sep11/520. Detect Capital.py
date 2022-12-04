class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        st = [ord(word[i]) < 97 for i in range(len(word))] 
        total = sum(st)
        if total == len(word) or total == 0 or total == 1 and st[0] == True:
            return True