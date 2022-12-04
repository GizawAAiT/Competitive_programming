class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left, right = [nums[0]], [nums[-1]]
        N = len(nums)
        for i in range(1, N):
            left.append(left[-1]+nums[i])
            right.insert(0,right[0]+nums[N-i-1])
        
        if N ==1 or right[1]==0: return 0
        for i in range(1,N-1): 
            if left[i-1] == right[i+1]:
                return i
        if left[-2]==0: return N-1
        return -1