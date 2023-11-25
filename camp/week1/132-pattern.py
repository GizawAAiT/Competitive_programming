class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        nums[0] = (nums[0], nums[0])
        for i in range(1, len(nums)):
            nums[i] = (nums[i], min(nums[i-1][1], nums[i]))
        
        h = []
        for i in range(len(nums)-1, -1, -1):
            num, p1 = nums[i]
            while h and h[0] <= p1:
                heappop(h)
            
            if h and p1 < h[0] < num: return True
            heappush(h, num)
        
        return False


         


        
