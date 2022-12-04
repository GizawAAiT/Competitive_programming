class Solution:
    def pivotIndex(self, nums: List[int]) -> int:      
        if len(nums)==1:
            return 0       
        pref, suf = [0], [0]
        for i in range(len(nums)-1):
            pref.append(pref[-1]+nums[i])
            suf.append(suf[-1]+nums[-1-i])
        suf = list(reversed(suf))
        for i in range(len(nums)):
            if pref[i]== suf[i]:
                return i
        return -1