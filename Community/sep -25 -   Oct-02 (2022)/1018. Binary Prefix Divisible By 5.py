class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        def calc(arr):
            p, total = len(arr)-1, 0
            while len(arr)>0:
                total += arr.pop(0)*2**p                    
                p-=1
            return total
        n = calc(nums.copy())
        
        res = []
        while n: 
            res.insert(0,n%5==0)
            n //= 2
        while nums[0]==0:
            res.insert(0,True)
            nums.pop(0)
        return res  
        