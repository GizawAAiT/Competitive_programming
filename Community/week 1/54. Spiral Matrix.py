class Solution(object):
    def spiralOrder(self, mat):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m1=n1=0
        m2=len(mat[0])-1
        n2=len(mat)-1
               
             
        A=[]
        while m1<m2 and n1<n2:
            i=m1
            while i<=m2:
                A.append(mat[n1][i])  
                i+=1
            n1+=1    
            j=n1
            while j<=n2:
                A.append(mat[j][m2])
                j+=1
            m2-=1

            k=m2
            while k>=m1:
                A.append(mat[n2][k])
                k-=1
            n2-=1
            l=n2
            while l>=n1:
                A.append(mat[l][m1])
                l-=1
            m1+=1
            
        if len(mat)==len(mat[0]) and len(mat)%2!=0:
            A.append(mat[m1][n1])
        elif len(mat)>len(mat[0]) and len(mat[0])%2!=0:
            for i in range(n1,n2+1):
                A.append(mat[i][m1])
        elif len(mat)<len(mat[0]) and len(mat)%2!=0:
            for i in range(m1,m2+1):
                A.append(mat[n1][i])
        return A