class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums = sorted(nums)
        ns = s = nums[0] + nums[1] + nums[-1]
        for a in range(len(nums)-2):
            i,j = a+1, len(nums)-1
            
            while i<j:
                s = nums[a] + nums[i] + nums[j]
                if s == target:
                    return target
                
                if abs(s-target) < abs(ns-target):
                    ns = s 
                    
                if s < target:
                    i += 1
                else:
                    j -=1
        return ns