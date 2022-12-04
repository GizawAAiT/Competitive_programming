class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        f, max_f ,res = {}, 1, 1
        for i in range(len(nums)):
            if nums[i] not in f:
                f[nums[i]] = [i]
            else:
                f[nums[i]].append(i)
                if len(f[nums[i]]) > max_f:
                    res = f[nums[i]][-1] - f[nums[i]][0] + 1 
                    max_f = len(f[nums[i]]) 
                elif len(f[nums[i]]) == max_f:
                    res = min(res, f[nums[i]][-1] - f[nums[i]][0] + 1 )
        return res 