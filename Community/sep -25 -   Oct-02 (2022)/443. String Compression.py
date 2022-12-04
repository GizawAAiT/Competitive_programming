class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)==1: return 1
        i, j = 0, 1  
        count=1
        while j<len(chars):
            if chars[i]!=chars[j]: 
                if count>1: 
                    for c in str(count):
                        chars.insert(j,c)
                        j+=1 
                    i =j
                    j=i+1
                    count=1
                else:i, j=i+1, j+1
                
            else:
                print((i,j))
                count+=1
                chars.pop(j)
                
        if count>1:
             for c in str(count):
                chars.append(c) 
        return len(chars)
            
                