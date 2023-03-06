class Solution:
    def hIndex(self, sits: List[int]) -> int:
        left = -1
        n = right = len(sits)
        while left < right - 1:
            mid = left + (right - left)//2
            if sits[mid] >= n-mid:
                right = mid
            else:
                left = mid
        return n-right

