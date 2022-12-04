class Solution(object):
    def longestSubarray(self, n, l):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int"""
        
        maxi=collections.deque([])
        mini=collections.deque([])
             
        
        i=j=0
        A=0
        while j<len(n):
            
            while mini and mini[-1]>n[j]:   
                mini.pop()
            mini.append(n[j])
            
            while maxi and maxi[-1]<n[j]:
                maxi.pop() 
            maxi.append(n[j])
            
            if maxi[0]-mini[0]<=l:
                
                A=max(A,j-i+1)
                
            else:
                if maxi[0]==n[i]:  
                    maxi.popleft()
                if mini[0]==n[i]:
                    mini.popleft()
                
                i+=1               
                
            j+=1
        
        return A
            
            
        
        