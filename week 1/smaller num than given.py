class Solution:
    def smallerNumbersThanCurrent(self, nums) :
        answer=[0]*len(nums)
        for i in range(len(nums)) :
            for j in nums:
                if nums[i]>j:
                    answer[i]+=1
        return answer
        
        