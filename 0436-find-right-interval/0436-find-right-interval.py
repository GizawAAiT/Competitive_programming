class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        dic = {}
        for i, interval in enumerate (intervals):
            dic[tuple(interval)] = i
        
        n = len(intervals) 
        sortedInterval = sorted(intervals)
        
        def getRightInterval(I):
            
            left = -1
            right = n
            while left < right - 1:
                mid = left + ( right - left )//2
                if sortedInterval[mid][0] >= I[1]:
                    
                    right = mid
                    print('did',right)
                else:
                    
                    left = mid
                    print('didnt',left,right,) 
            return dic[tuple(sortedInterval[right])] if right != n else -1
        
        return [getRightInterval(I) for I in intervals]
        
                    
