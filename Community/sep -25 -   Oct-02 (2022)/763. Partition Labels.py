class Solution:
      
    def partitionLabels(self, s: str) -> List[int]:
        ind={}
        for i in range(len(s)):
            ind[s[i]]=i 
       
        index = [ind[i] for i in s]
        print(index)
        st=[]
        mx=index[0]
        for i in range(len(index)):
            mx=max(mx,index[i])
            if mx<=i:
                v=i+1 if not st else i+1-sum(st)
                st.append(v)  
        return st