class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss = {}
        for winner, losser in matches:
            if winner not in loss:
                loss[winner] = 0
            if losser not in loss:
                loss[losser] = 0
            loss[losser] +=1
        
        ans = [[], []]
        for k in sorted(loss):
            if loss[k] <2:
                ans[loss[k]].append(k)
        return ans