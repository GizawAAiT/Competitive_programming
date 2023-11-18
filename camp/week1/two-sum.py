class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for indx, num in enumerate(nums):
            if target-num in dic:
                return [dic[target-num], indx]
            dic[num] = indx
        