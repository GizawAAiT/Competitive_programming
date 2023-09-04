class Solution(object):
    def nextGreaterElement(self, m, n):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        st=[]
        dict={}
        a=[]
        for i in range(len(n)):
            while len(st)!=0 and st[-1]<n[i] : 
                
                
                if len(st)!=0:
                    dict[st[-1]]=n[i]
                st.pop()
            st.append(n[i])
        for i in st:
            dict[i]=-1
        for i in m:
            
            a.append(dict[i])
            
        return a
            
                
                    