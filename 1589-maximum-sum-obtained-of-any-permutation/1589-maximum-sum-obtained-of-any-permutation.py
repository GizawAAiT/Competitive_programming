class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        pref = [0 for i in range(len(nums)+1)]
        
        for r in requests:
            pref[r[0]] += 1
            pref[r[-1]+1] -= 1
        for i in range(1, len(pref)):
            pref[i] += pref[i-1]
        pref.pop()
        nums.sort()
        pref.sort()
        return sum([nums[i]*pref[i] for i in range(len(nums)) ] )%(10**9+7)
     