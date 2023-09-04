class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)==2:
            return min(cost)
        Dp = [cost[-1],cost[-2]]
        
        for i in range(len(cost)-2):
            Dp.append(cost[-3-i]+min(Dp[-1],Dp[-2]))
        
        print(f"Dp : {Dp}")
        return min(Dp[-2],Dp[-1])