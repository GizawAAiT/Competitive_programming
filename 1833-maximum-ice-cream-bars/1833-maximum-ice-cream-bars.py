class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        
        i = 0 
        while i<len(costs) and costs[i]<=coins: 
            coins -= costs[i]
            i+=1
        return i
    