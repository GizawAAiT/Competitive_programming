class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] %=2
        
        left = 0
        while left < len(nums) and nums[left ]==0:
            left += 1
        
        ones = res = 0
        for right in range(left, len(nums)):
            ones += nums[right]
            if ones == k:
                l, r = left-1, right+1
                while l>=0 and nums[l] == 0:
                    l-=1
                while r<len(nums) and nums[r] == 0:
                    r+=1
                res += (left-l ) * (r - right)
                print(((l,left), (right,r)))
                # print((left-l ) * (r - right))
                left += 1
                while left < len(nums) and nums[left ]==0:
                    left += 1
                ones -= 1
        return res
            