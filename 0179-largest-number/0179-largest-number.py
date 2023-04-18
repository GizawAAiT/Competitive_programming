class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        nums = [str(i) for i in nums] 
        
        for i in range(1, n):
            j = i-1
            while j > -1 and int(nums[j+1]+nums[j]) > int(nums[j]+nums[j+1]) :
                nums[j], nums[j+1] = nums[j+1], nums[j]
                j -= 1
                # print(nums)
            
        return str(int(''.join(nums)))
                
        