class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = True
        for i in nums:
            if i ==0:
                return 0
            elif i < 0:
                sign = not sign 
        return 1 if sign else -1