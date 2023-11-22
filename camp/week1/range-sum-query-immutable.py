class NumArray:

    def __init__(self, nums):
        self.nums = nums
        for i in range(1, len(self.nums)):
            self.nums[i] += self.nums[i-1]

    def sumRange(self, l, r):
        return self.nums[r] if l == 0 else self.nums[r] - self.nums[l-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)