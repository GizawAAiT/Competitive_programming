class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        
        st = []
        
        for i in range(1,len(s)+1):
            n = dict[s[-i]]
            if st and n < st[-1]:
                st.append(-n)
            else:
                st.append(n)
        return sum(st)