'''Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums.append(-1)
        def cycle_sort():
            for indx in range(len(nums)):

                while nums[indx] != indx : 
                    if nums[indx] == -1: break
                    nums[nums[indx]], nums[indx] = nums[indx], nums[nums[indx]]
        
        
        cycle_sort()
        
        for i in range(len(nums)):
            if nums[i] == -1:
                return i
        