class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total = sum([i for i in nums if i%2==0])
        res = []
        for q in queries:
            num = 0
            if not nums[q[1]]%2:
                total -= nums[q[1]]
            nums[q[1]] += q[0]
            if not nums[q[1]]%2:
                total += nums[q[1]]
            res.append(total)
        return res