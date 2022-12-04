class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==3 and sum(nums)==0:
            return [nums]
        nums = sorted(nums)
        triplets = []
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            a, b = i+1, len(nums)-1
            while a<b:
                sm = nums[a] + nums[b] + nums[i] 
                if sm==0:
                    triplets.append([nums[i],nums[a],nums[b]])
                    a+=1
                    b-=1
                    while a<b and nums[a]==nums[a-1]:
                        a+=1
                elif sm < 0:
                    a+=1
                    
                else:
                    b-=1
        print(nums)
        return triplets
                    



        
        