class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tot, cur, resIndex =0, 0,  0
        for i in range(len(gas)):
            cur += gas[i]-cost[i]
            tot += gas[i]-cost[i]
            if cur<0:
                resIndex, cur = i+1, 0
        if tot >= 0 : return resIndex
        return -1
                