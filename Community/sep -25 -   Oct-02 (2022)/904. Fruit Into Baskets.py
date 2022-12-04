class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits)<3: 
            return len(fruits)
        res, i, j = 0, 0, 1
        bin=[fruits[0]] 
        while j<len(fruits):
            if len(bin)==2 and fruits[j] not in bin:
                res=max(res,j-i)
                i=j-1
                while i>0 and fruits[i]==fruits[j-1]:
                    i-=1                
                bin.remove(fruits[i])
                i+=1
                bin.append(fruits[j])
            elif fruits[j] in bin:
                j+=1
            else:
                bin.append(fruits[j])
                j+=1
        
        res=max(res,j-i) 
        return res
        