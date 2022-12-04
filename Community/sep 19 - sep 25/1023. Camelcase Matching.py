class Solution:
    def camelMatch(self, qu: List[str], pa: str) -> List[bool]:
        
        def match(qu,pa):
            pa = list(pa)
            i = 0
            while pa and i<len(qu):                
                if qu[i]==pa[0]:
                    pa.pop(0)
                elif qu[i].isupper():
                    return False
                i+=1 
            if pa:
                return False
            while i<len(qu):
                if qu[i].isupper():
                    return False
                i+=1
            
            return True
        return [match(qu[i],pa) for i in range(len(qu))] 
    
            
    