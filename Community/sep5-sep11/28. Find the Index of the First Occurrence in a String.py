class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a,b = 0,0
        
        while a < len(haystack):  
            if haystack[a] == needle[0]:
                tempo = a
                while b < len(needle) and a <len(haystack) and haystack[a] == needle[b]: 
                    a+=1
                    b+=1
                if b==len(needle):
                    return a-b
                a = tempo + 1
                b=0
            else:
                a+=1
        return -1
                