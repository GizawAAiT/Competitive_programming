class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) ==1:
            return [-1]
        greater = {nums2[-1]: -1}
        mx = [nums2[-1]]
        i = len(nums2)-2        
        while i >= 0:
            if nums2[i] < mx[-1]:                 
                greater[nums2[i]] = mx[-1]
                mx.append(nums2[i])
            else:
                while mx and mx[-1]< nums2[i]: 
                    mx.pop()
                if not mx:
                    greater[nums2[i]] = -1
                else:
                    greater[nums2[i]] = mx[-1]
                mx.append(nums2[i])
                    
            i-=1
            # print(greater.values())
        ans = [greater[i] for i in nums1] 
        return ans
        