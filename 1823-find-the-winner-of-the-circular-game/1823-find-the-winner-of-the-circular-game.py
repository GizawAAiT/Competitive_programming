class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [_ for _ in range(1,n+1)]
        i = 0
        # print(nums)
        while len(nums)>1:
            i = (i+k-1)%len(nums)
            # print(nums)
            nums.pop(i)  
        return nums[0]