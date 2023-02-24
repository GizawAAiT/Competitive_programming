class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]
        suf = [1]
        
        for i in range(len(nums)-1):
            pref.append(pref[-1]* nums[i])
            suf.append(suf[-1] * nums[-1-i])
        suf.reverse()
        print(pref,'\n',suf)
        
        # pref.pop(0)
        # suf.pop()
        # a = [1,2,3,1,2,3]
        # [0,1,3,6...].reverse() = [...6, 13,2,0]
        
        return [pref[i] * suf[i] for i in range(len(nums))]