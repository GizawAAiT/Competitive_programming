class Solution:
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = None
        def quick_sort(left, right):
            # print('quick_sort clled with.', (left, right), nums)
            nonlocal result
            pivot = nums[left]
            writter = left + 1
             
            for reader in range(left + 1, right): 
                if nums[reader] <= pivot:
                    nums[reader], nums[writter] = nums[writter], nums[reader]
                    writter += 1
            
            nums[writter-1], nums[left] = pivot, nums[writter-1]
            if writter - 1 == n-k: 
                result = pivot
                return
            if n-k < writter:
                quick_sort(left, writter-1)
            else:
                quick_sort(writter, right)
                
        quick_sort(0, n)
        
        return result
        
            
            