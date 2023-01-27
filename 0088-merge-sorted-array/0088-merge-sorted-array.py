class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        new = nums1[:m]
        i=j= k = 0

        while j<len(new) and k<len(nums2):
            if new[j]<=nums2[k]: 
                nums1[i]= new[j]
                j+=1
            else: 
                nums1[i]= nums2[k]
                k+=1
            i+=1
        
        while j<len(new):
            nums1[i]= new[j]
            j+=1
            i+=1
            
        while k<len(nums2):
            nums1[i] = nums2[k]
            k+=1
            i+=1
    
