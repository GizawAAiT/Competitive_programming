class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0]*len(nums2) for _ in range(len(nums1))]
        
        maxVal = 0
        for i in range(len(nums1)):
            dp[i][0] += nums1[i] == nums2[0]
            maxVal = max(maxVal, dp[i][0])

        for j in range(1, len(nums2)):
            dp[0][j] += nums1[0] == nums2[j]
            maxVal = max(maxVal, dp[0][j])
        
        for i in range(1, len(nums1)):
            for j in range(1, len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[i][j] += dp[i-1][j-1] + 1
                    maxVal = max(maxVal, dp[i][j])
                    
        return maxVal
        