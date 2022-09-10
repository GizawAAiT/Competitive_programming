class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:        
        nums = sorted(nums)
        d = {nums[0]:1}
        
        index = 1
        while index < len(nums):
            if nums[index]== nums[index-1]:
                d[nums[index]]+=1    
                nums.pop(index)
            else:
                d[nums[index]]=1
                index +=1
        
        if len(nums)==1 or len(nums)==2 and nums[0]!=nums[1]-1:
            new = [i*d[i] for i in nums]
            return sum(new)
        if len(nums)==2 and nums[0]==nums[1]-1:
            return max(nums[1]*d[nums[1]],nums[0]*d[nums[0]])
        
        Dp = [nums[0]*d[nums[0]]]
        if nums[0]==nums[1]-1:
            Dp.append(max(Dp[0],nums[1]*d[nums[1]]))
        else:
            Dp.append(nums[1]*d[nums[1]]+Dp[0])
        
        i = 2
        while i < len(nums):
            if nums[i]==nums[i-1]+1:
                Dp.append(max(Dp[-1],Dp[-2]+nums[i]*d[nums[i]]))
            else:
                Dp.append(Dp[-1]+nums[i]*d[nums[i]])
            i+=1
        print(Dp)
        print(f"nums {nums}\n d {d.values()}")
        return Dp[-1]