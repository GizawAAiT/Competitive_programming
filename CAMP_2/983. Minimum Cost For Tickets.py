class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def dp(indx):
            if indx >= len(days):
                return 0
            seven_indx, thirty_indx = indx, indx
            while seven_indx < len(days)  and days[seven_indx] - days[indx]<7:
                seven_indx += 1
            while thirty_indx < len(days)  and days[thirty_indx] - days[indx] <30:
                thirty_indx += 1
    

            one_day_pass = costs[0] + dp(indx+1)
            seven_day_pass = costs[1] + dp(seven_indx)
            thirty_day_pass = costs[2] + dp(thirty_indx)
            return min(one_day_pass, seven_day_pass, thirty_day_pass)
        return dp(0)