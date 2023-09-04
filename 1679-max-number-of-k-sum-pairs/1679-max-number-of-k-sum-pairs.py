class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums)-1
        res = 0
        while l<r:
            t = nums[l] + nums[r]
            if t == k:
                res +=1
                l+=1
                r-=1
            elif t < k:
                l+=1
            else:
                r-=1
        return res
        