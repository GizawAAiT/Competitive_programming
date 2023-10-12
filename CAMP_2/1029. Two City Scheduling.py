class Solution:
    def __init__(self):
        self.n = 0
        # self.answer = float("inf")
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # recursion(citya, counta, cityb, countb)
        self.n = len(costs)//2
        
        @cache
        def recur(count_a, count_b):
            indx = count_a + count_b
            if indx >= 2*self.n:
                return 0
            
            cost_a = cost_b = float("inf")
            if count_a < self.n: 
                cost_a = costs[indx][0] + recur(count_a+1, count_b) 
            if count_b < self.n:
                cost_b = costs[indx][1] + recur(count_a, count_b+1)    
   
            return min(cost_a, cost_b)

        return recur(0, 0)
