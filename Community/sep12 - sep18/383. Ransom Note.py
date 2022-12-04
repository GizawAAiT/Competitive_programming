class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        ransomNote = sorted(list(ransomNote))
        magazine = sorted(list(magazine))
        m, r = 0, 0
        while r < len(ransomNote) and m < len(magazine):
            if magazine[m] != ransomNote[r]: 
                if m == len(magazine)-1: 
                    return False
                m +=1 
            else:
                m +=1
                r +=1
        print(ransomNote,"\n",magazine)
        return True if r == len(ransomNote) else False
            