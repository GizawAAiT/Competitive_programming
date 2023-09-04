class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        i=0
        j=0
        st=[]
        
        for i in range(len(pushed)):
            st.append(pushed[i])
            
            while len(st)!=0 and popped[j]==st[-1]:
                st.pop()
                j+=1
                
        
                
        if len(st)==0 and i+1==j:
            return True
        return False
            