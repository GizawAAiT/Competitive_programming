class Solution:
    def freqAlphabets(self, s: str) -> str:
        d={}
        
        for i in range(ord("z")-ord("a")+1):
            d[str(i+1)]=chr(i+ord("a"))
        # print("keys:::",d.keys())
        output=[]
        i=len(s)-1
        while i>=0:
            # print(i)
            if s[i]=="#":    
                output.append(d[s[i-2:i]]) 
                i-=3
            else: 
                output.append(d[s[i]])   
                i-=1
        
        return "".join(list(reversed(output)))