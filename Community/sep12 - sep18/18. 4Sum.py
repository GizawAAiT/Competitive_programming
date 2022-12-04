class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums)<4:
            return []
        nums.sort()
        
        quadruplets = []
        for i in range(len(nums)-3):
            if i>0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j>i+1 and nums[j]== nums[j-1]:
                    continue
                two = nums[j] + nums[i]
                a, b = j+1, len(nums)-1
                    
                while a < b:
                    
                    s = two + nums[a]+ nums[b]
                    if s == target:
                        quadruplets.append([nums[i],nums[j],nums[a],nums[b]])
                        a, b = a+1, b-1
                        while a<len(nums)-1 and nums[a]==nums[a-1]:
                            a+=1
                    elif s < target:
                        a+=1
                    else:
                        b-=1
        return quadruplets                
                    
        
