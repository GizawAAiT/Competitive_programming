class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res =  sum([min(tickets[k], t) for t in tickets])
        # if res > len(tickets):
        for i in range(k+1, len(tickets)):
            if tickets[i]>=tickets[k]:
                res -=1
        return res