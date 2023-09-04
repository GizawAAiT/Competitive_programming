class Solution:
    def nextGreaterElements(self, nums):
        stack = [0]
        n = len(nums)
        dic = {}
        for i in range(1, 2*n):
            while stack and nums[i%n] > nums[stack[-1]]:
                dic[stack.pop()] = nums[i%n] 
                # stack.pop()
            stack.append(i%n)
        while stack:
            if stack[-1] not in dic:
                dic[stack.pop()] = -1
            else:
                stack.pop()
        return [dic[i] for i in range(n) ]
         