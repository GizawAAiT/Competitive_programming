class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = neg = 0
        arranged = []
        
        N = len(nums)
        for i in range(N):
            while pos<N and nums[pos]<0: pos+=1
            while neg<N and nums[neg]>0: neg+=1
            
            if i%2:  
                arranged.append(nums[neg])
                neg+=1
            else:
                arranged.append(nums[pos])
                pos+=1
        return arranged
                