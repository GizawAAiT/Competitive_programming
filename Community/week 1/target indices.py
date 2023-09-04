class Solution:
    def targetIndices(self, nums, target):
        answer=[]
        for i in range(len(nums)):
        
            for j in range (i+1,len(nums)):
                if nums[i]>nums[j]:
                    (nums[i],nums[j])=(nums[j],nums[i])
        for i in range(len(nums)):
            if nums[i]==target:
                answer.append(i)

        return answer
    
        