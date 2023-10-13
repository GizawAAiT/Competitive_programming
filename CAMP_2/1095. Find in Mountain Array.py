# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        def pivot():
            l, r = 0, mountain_arr.length()-1
            while l<r:
                mid = l + (r-l)//2
                middle_val = mountain_arr.get(mid) 
                left_val, right_val = mountain_arr.get(mid-1), mountain_arr.get(mid+1)
                if left_val < middle_val and middle_val > right_val:
                    return mid
                
                if left_val < middle_val:
                    l = mid
                else:
                    r = mid
                
        def getMinIndex(l, r, increasing): #isIncreasing is true for the first half and false for the second half 
            while l<r-1:
                mid = l+(r-l)//2
                mid_val = mountain_arr.get(mid)
            
                if (increasing and mid_val < target) or (not increasing and mid_val > target):
                    l = mid
                else:
                    r = mid
            if mountain_arr.get(r) == target:
                return r
            return -1
        
        # find the pivot:
        piv = pivot()
        min_indx = getMinIndex(-1, piv, True)
        if min_indx != -1:
            return min_indx
        return getMinIndex(piv, mountain_arr.length()-1, False)
            
                


