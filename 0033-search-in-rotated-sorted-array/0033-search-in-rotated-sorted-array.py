class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def piv(left, right):
            while left < right-1: 
                middle = left + (right - left) // 2
                if nums[middle] > nums[left]:
                    left = middle
                else:
                    right = middle
            return right 
        
        def binary(left, right):
            if target < nums[left] or target > nums[right]: return -1 
            if nums[left ] == target: return left
            if nums[right] == target: return right
            
            while left < right-1:
                middle = left + (right - left) // 2
                
                if nums[middle ] == target:
                    return middle
                if nums[middle] < target:
                    left = middle
                else:
                    right = middle
                
                if left == right: return -1
            return -1
        
        if nums[0] < nums[-1]:
            return binary(0, len(nums)-1)
        
        pivot = piv(0, len(nums)-1)
        if nums[0] > target:
            return binary(pivot, len(nums)-1) 
        return binary(0, pivot-1)
    
        