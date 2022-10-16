class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cur_sum = sum(arr[:k])
        i, j = 0, k
        res = int(cur_sum/k>=threshold)
        while j<len(arr):            
            cur_sum += (arr[j]-arr[i])
            i, j = i+1, j+1
            res += int(cur_sum/k >= threshold)
        return res