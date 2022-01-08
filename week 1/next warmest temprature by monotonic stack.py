class Solution(object):
    def dailyTemperatures(self, n):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        st=[0]
        dict={}
        a=[]
        for i in range(1,len(n)):
            while len(st)!=0 and n[st[-1]]<n[i] : 
                dict[st[-1]]=i-st[-1]
                st.pop()
            st.append(i)
        for i in st:
            dict[i]=0
        for i in range(len(n)):
            a.append(dict[i]) 

        return a