class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        c = 0
        i = 1
        while i < len(intervals):
            if intervals[i][0] < intervals[i-1][1]:
                intervals.pop(i-int(intervals[i][1]<intervals[i-1][1]))
                c +=1
            else:
                i+=1
        return c
           