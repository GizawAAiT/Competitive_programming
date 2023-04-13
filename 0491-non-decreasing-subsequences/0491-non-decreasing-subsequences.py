class Solution:
    def __init__(self):
        self.result = set()
        
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        path = []
        def backtrack(start):
            
            if len(path) > 1:
                self.result.add(tuple(path[:])) 
                
            for index in range(start, len(nums)):
                if not path or nums[index] >= path[-1]: 
                    path.append(nums[index])
                    backtrack(index+1)
                    path.pop()
            
        backtrack(0)
        return  self.result
            