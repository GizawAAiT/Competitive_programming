class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        if len(arr) ==1:
            return arr[0]
        ans = 0
        for i in range(len(arr)):
            ans += arr[i]
            lsum, j = arr[i], i
            while j+2 < len(arr):
                lsum += (arr[j+1]+ arr[j+2])
                j+=2
                ans += lsum
        return ans
            