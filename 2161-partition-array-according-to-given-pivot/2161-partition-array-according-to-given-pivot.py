class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        piv = 0
        while nums[piv] != pivot:
            piv +=1
        
        # collect all element>pivot to the right of piv.
        i = piv-1
        print(piv, nums[piv])
        while i>=0:
            if nums[i] > pivot:
                nums.insert(piv, nums.pop(i))
                print(piv, nums[piv])
                piv -=1
            i-=1
        i = piv+1
        while i<len(nums):
            if nums[i] < pivot:
                nums.insert(piv, nums.pop(i))
                print(piv, nums[piv])
                piv +=1
            i+=1
        i = piv+1
        while i<len(nums) and nums[i]==pivot:i+=1
            
        while i<len(nums):
            if nums[i] == pivot and i>piv+1:
                nums.insert(piv+1, nums.pop(i))
                print(piv, nums[piv])
                piv +=1
            i+=1
        return nums
        
        # collect all elements < pitot to the left of piv.
        
        # collct all elements == pivot to the right of piv.
        