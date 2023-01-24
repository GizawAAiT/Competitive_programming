class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l<r:
            dimr = numbers[l] +numbers[r]
            if dimr == target:
                return [l+1, r+1]
            if dimr < target:
                l+=1
            else:
                r-=1
        