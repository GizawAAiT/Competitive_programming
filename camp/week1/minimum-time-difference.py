class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for time in timePoints:
            h, m = (int(_) for _ in time.split(':'))
            minutes.append(h*60 + m)
        
        minutes.sort()
        ans = 12*60
        for i in range(len(minutes)):
            diff = abs(minutes[i]-minutes[i-1])
            ans = min(ans, min(diff, 24*60-diff))
        
        return ans

