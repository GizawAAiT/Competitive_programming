class Solution:
    def findPoisonedDuration(self, time: List[int], dur: int):
        if len(time)==1: return dur
        res=0
        for i in range(len(time)-1):
            res+=min(time[i+1]-time[i],dur)
        return res+dur
    