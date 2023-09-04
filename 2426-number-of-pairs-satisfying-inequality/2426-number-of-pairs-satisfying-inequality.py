class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        
        nums = [nums1[i]-nums2[i] for i in range (len(nums1))]
        def merge_sort(nums):
            nonlocal count
            if len(nums) <= 1:  
                return 
            
            mid_ = len(nums)//2
            left_sub, right_sub = nums[ : mid_], nums[mid_ : ]
            
            merge_sort(left_sub)
            merge_sort(right_sub)
            
            j = 0
            for i in range(len(left_sub) ):
                while j < len(right_sub) and left_sub[i] - right_sub[j] >  diff : 
                    j += 1
                    
                count += len(right_sub) - j 
                                       
            
            # merging.
            i, j, k = 0, 0, 0
            while i < len(left_sub) and j < len(right_sub):
                if left_sub[i] <= right_sub[j]:
                    nums[k] = left_sub[i]
                    i += 1
                else:
                    nums[k] = right_sub[j]
                    j += 1
                k += 1
            
            while i < len(left_sub):
                nums[k] = left_sub[i]
                i += 1
                k += 1
                
                
            while j < len(right_sub):
                nums[k] = right_sub[j]
                j += 1
                k += 1
        
        count = 0
        merge_sort(nums)
        return count
            
            
            