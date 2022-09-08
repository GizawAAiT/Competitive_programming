class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = [0]
        
        for n in nums:
            runningSum.append(runningSum[-1]+ n)
        return runningSum[1:]