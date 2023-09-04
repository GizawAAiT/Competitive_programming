class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True) 
        left = -1
        right = len(citations)
        while left<right-1:
            mid = left + (right-left)//2
            if mid+1 > citations[mid]:
                right = mid
            else:
                left = mid
        return left + 1