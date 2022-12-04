class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pointer1 = pointer2 = 0
        while pointer2 <len(nums):
            if nums[pointer2]!=0:
                temp=nums[pointer2]
                nums.pop(pointer2)
                nums.insert(pointer1,temp)
                pointer1 +=1
                pointer2 +=1
            else:
                pointer2 +=1
        return nums
            
        