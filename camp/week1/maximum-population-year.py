class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        prefix = [0 for _ in range(101)]
        for birth, death in logs:
            prefix[birth-1950] += 1
            prefix[death-1950] -= 1
        
        # prefix
        maxIndx = 0
        for i in range(1, 101):
            prefix[i] += prefix[i-1]
            if prefix[i] > prefix[maxIndx]:
                maxIndx = i
        return maxIndx + 1950
        

