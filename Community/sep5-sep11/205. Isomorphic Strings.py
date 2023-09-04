class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        reverse = {}
        i = 0
         # s to t
        while i < len(s):
            exist = s[i] in mapping.keys() 
            if exist and t[i]!=mapping[s[i]]:  
                return False          
            if not exist:
                mapping[s[i]]= t[i]
            i+=1
         # s to t
        i = 0 
        while i < len(s):
            exist = t[i] in reverse.keys() 
            if exist and s[i]!=reverse[t[i]]:  
                return False          
            if not exist:
                reverse[t[i]]= s[i]
            i+=1
        return True