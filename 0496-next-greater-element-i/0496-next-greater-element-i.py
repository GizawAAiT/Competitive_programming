class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        
        greaterHash = {}
        min_stack = []
        for n in nums2:
            while min_stack and n>min_stack[-1]:
                greaterHash[min_stack.pop()] = n
            min_stack.append(n)
        while min_stack:
            greaterHash[min_stack.pop()] = -1
        return [greaterHash[n] for n in nums1]