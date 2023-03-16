class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []       
        arr = [[], 0]
        def backtrack(arr, i):
            if arr[1] == target:  
                result.append(arr[0][:])
                return
             
            for idx in range(i,len(candidates)): 
                n = candidates[idx]
                if arr[1] + n <= target:  
                    arr[1] += n
                    arr[0].append(n)
                    backtrack(arr, idx)  
                    arr[0].pop()
                    arr[1] -= n 
                    
                else:
                    break
        backtrack(arr, 0) 
        return result
                
            