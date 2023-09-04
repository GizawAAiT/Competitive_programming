class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
            
        m = self.bin(nums,target)   
        if m == None or not nums:
            return [-1,-1]
        a=b=m
        while a>0 and nums[a-1] == target:
            a-=1
        while b<len(nums)-1 and nums[b+1] == target:
            b+=1  
            
        return [a,b]
    
    def bin(self,n,t):
        a,b = 0,len(n)-1
        
        if n[a] == t:
            return a
        elif n[b] == t:
            return b
        while a<b-1:
                middle = (a+b)//2
                if n[middle] == t:
                    return middle
                elif t < n[middle]:
                    b = middle                
                else:
                    a = middle
        return None
                