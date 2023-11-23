class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binarySearchReplacement(nums, num):
            l, r = -1, len(nums)-1
            while l<r-1:
                mid = l + (r-l)//2
                if nums[mid] >= num:
                    r = mid
                else: l = mid
            nums[r] = num
        
        res = []
        for num in nums:
            if not res or res[-1] < num:
                res.append(num)
            else:
                binarySearchReplacement(res, num)
            # print(res)
        return len(res)
        
