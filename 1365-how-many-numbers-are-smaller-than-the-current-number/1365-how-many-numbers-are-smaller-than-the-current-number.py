class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dic = {}
        nums2 = sorted(nums)
        for i in range(n-1, -1, -1):
            dic[nums2[i]] = i
        return [dic[nums[_]] for _ in range(n)]
        