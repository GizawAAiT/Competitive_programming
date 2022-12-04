class Solution:
    def trap(self, nums: List[int]) -> int:
        left_max = [nums[0]]
        right_max = [nums[-1]]
        sea_level = []
        for i in range(1,len(nums)):
            left_max.append(max(left_max[-1],nums[i-1]))
            right_max.append(max(right_max[-1],nums[-i]))
        right_max = list(reversed(right_max))
        for i in range(len(nums)):
            sea_level.append(min(left_max[i],right_max[i]))
        print(sea_level)
        
        volume = 0
        
        for i in range(len(nums)):
            if sea_level[i]-nums[i] > 0: 
                volume+=(sea_level[i]-nums[i])
        return volume