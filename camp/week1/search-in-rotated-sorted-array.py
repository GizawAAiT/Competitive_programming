class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary(l, r):
            while l < r-1:
                mid = l + (r-l)//2
                if nums[mid] == target: return mid
                if nums[mid] < target:
                    l = mid
                else: r = mid
            
            return -1
        
        l, r = -1, len(nums)
        while l < r-1:
            mid = l + (r-l)//2
            if nums[mid] > nums[-1]:
                l = mid
            else: r = mid

        a, b = binary(l, len(nums)), binary(-1, r)
        return a if a != -1 else b

        
