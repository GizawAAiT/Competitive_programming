class Solution(object):
    def minIncrementForUnique(self, n):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=sorted(n)
        st=[]
        st.append(n[0])
        c=0
        for i in range( 1,len(n)):
            if st[-1]+1>n[i]:
                c+=st[-1]+1-n[i]
                st.append(st[-1]+1)
            else:
                st.append(n[i])
        return c