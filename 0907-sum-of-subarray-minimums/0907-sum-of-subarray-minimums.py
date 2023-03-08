class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr.insert(0, 0)
        arr.append(0)
        
        stack = []
        res = 0
        
        for i, v in enumerate(arr):
            while stack and v < arr[stack[-1]]:
                res += (arr[stack[-1]] * (stack[-1] - stack[-2]) * (i-stack[-1]))
                stack.pop()
            stack.append(i)
            
        return res%(10**9+7)
        
                    