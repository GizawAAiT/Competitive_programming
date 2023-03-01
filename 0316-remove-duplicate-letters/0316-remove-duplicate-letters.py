class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dic = Counter(s)
        stack = []
        hashSet = set()
        for char in s:
            if char not in hashSet:  
                while hashSet and char <= stack[-1] and dic[stack[-1]]>0:
                    c = stack.pop()
                    hashSet.remove(c)
                stack.append(char)
                hashSet.add(char) 
            dic[char] -=1
            
            
            
        return ''.join(stack) 
                
                