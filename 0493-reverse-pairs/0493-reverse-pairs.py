class Solution:
    def __init__(self):
        self.count = 0
    def reversePairs(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        half_ = len(nums) // 2

        # split the nums into two halfs.
        left_half, right_half = nums[ : half_], nums[half_ : ]
        
        self.reversePairs(left_half)
        self.reversePairs(right_half)
        
        j = 0
        for i in range(len(left_half)):
            while j < len(right_half) and 2*right_half[j] < left_half[i]:
                j += 1
            self.count += j
        

        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                nums[k] = left_half[i]
                i += 1
            else:
                nums[k] = right_half[j]
                j += 1
            k += 1
            
        while i < len(left_half):
            nums[k] = left_half[i]
            i += 1
            k += 1
            
        while j < len(right_half):
            nums[k] = right_half[j]
            j += 1
            k += 1
        
        return self.count
        
    
        