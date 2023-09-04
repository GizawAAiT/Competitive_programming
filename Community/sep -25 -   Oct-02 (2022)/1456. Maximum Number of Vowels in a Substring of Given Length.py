class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a","e",'i','o','u'}
        res = 0
        for char in s[:k]:
            if char in vowels: res +=1
        
        i, j = 0, k
        cur_val = res
        while j<len(s):
            cur_val += (int(s[j] in vowels)-int(s[i] in vowels))
            res = max(res, cur_val)
            i, j = i+1, j+1
            
        return res