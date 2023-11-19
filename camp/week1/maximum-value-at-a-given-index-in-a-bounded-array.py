class Solution:
    def maxValue(self, n: int, indx: int, maxSum: int) -> int:
        def area (t):
            l, r = min(t-2, indx), min(t-2, n-1-indx)
            # print(f'l, r = {l,r} for mid = {t}')
            return t + (l/2)*(t-1 + t-l) + max(0, indx-l) + (r/2)*(t-1 + t-r) + max(0, n-1-r-indx)
        
        left, right = 1, maxSum+1
        while left<right-1:
            mid = left + (right-left)//2
            # print(f'mid: {mid}, area:{area(mid)}')
            if area(mid) <= maxSum:
                left = mid
            else:
                right = mid
        return left


