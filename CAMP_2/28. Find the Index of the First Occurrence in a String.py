class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)

        # LPS
        lps = [0]*m # longest prefix-suffix:
        left, right = 0, 1
        while right < m:
            if needle[left] == needle[right]:
                lps[right] = left + 1
                left += 1
                right += 1

            elif left > 0: 
                left = lps[left-1]
            else:
                right += 1

            
        # Matching:
        i = j = 0
        while j < n:
            if needle[i] == haystack[j]:
                i += 1
                j+= 1
            elif i > 0:
                i = lps[i-1]
            else: 
                j += 1
            
            if i == m:
                return j-i

        return -1


        
        # n, m = len(haystack), len(needle)
        # if n < m : return -1

        # def pollFirst(hash_val, char, length):
        #     return hash_val - (ord(char)-96) *(27**length)

        # def addLast(hash_val, char, length):
        #     return hash_val * 27 + ord(char)-96 

        # pattern = 0
        # power = len(needle)-1
        # for char in needle:
        #     pattern += (ord(char)-96) * 27**power
        #     power -= 1
        
        # left , right = 0,  0
        # cur = 0
        # while right < n:
        #     length = right - left
        #     if right - left< m:
        #         cur = addLast(cur, haystack[right], length)
        #     else:
        #         cur = addLast(cur, haystack[right], length)
        #         cur = pollFirst(cur, haystack[left], length)  
        #         left += 1
        #     right += 1
        #     print(left, right)
        #     print(pattern, cur)
        #     if cur == pattern:
        #         return left

        # return -1


