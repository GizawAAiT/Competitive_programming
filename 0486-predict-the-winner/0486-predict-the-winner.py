class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def backtrack(s1, s2, l, r, p1):
            if l>r:
                print((l,r))
                return s1>=s2
            if p1:
                a = s1 + nums[l]
                b = s1 + nums[r]
                p1 = not p1
                return backtrack(a, s2, l+1, r, p1) or backtrack(b, s2, l, r-1, p1)
            else:
                a = s2 + nums[l]
                b = s2 + nums[r]
                p1 = not p1
                return backtrack(s1, a, l+1, r, p1) and backtrack(s1, b, l, r-1, p1)
        
        return backtrack(0, 0, 0, len(nums)-1, True)
    