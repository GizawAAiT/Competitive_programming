from sortedcontainers import SortedList
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        n, candidates, ans = len(nums), SortedList(), float('inf')
        for i in range(x, n):
            candidates.add(nums[i-x])

            l, r = 0, len(candidates)
            while l< r-1:
                mid = l+(r-l)//2
                if candidates[mid] < nums[i]:
                    l = mid
                else: r = mid 

            ans = min(ans, abs(candidates[l]-nums[i]))    
            if l < len(candidates)-1:
                ans = min(ans,abs(candidates[l+1]-nums[i]))  
        
        return ans
