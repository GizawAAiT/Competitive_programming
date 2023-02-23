class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        for _ in range(1, len(nums)):
            self.nums[_] += self.nums[_-1]
        self.nums.insert(0, 0)
    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right+1] - self.nums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)