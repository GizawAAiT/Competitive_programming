class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1:return 0 if nums[0]==target else -1
        
        t=1
        while t+1<=len(nums) and nums[-1-t]<nums[-t]:
            t+=1
            print("t:",t)
        t=0 if t==1 else t
        print("t final:",t)
        for i in range(-t,-t+len(nums)):
            if nums[i]==target: return i if i>=0 else i+len(nums)
        return -1
                
        