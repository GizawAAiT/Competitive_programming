class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        for i in range(len(ages)):
            ages[i] = [ages[i], scores[i]]

        ages.sort()
        @cache
        def recur(indx, lim):

            if indx >= len(ages):
                return 0
            
            if ages[indx][1] < lim:
                return recur(indx+1, lim)
            else:
                return max(recur(indx+1, ages[indx][1]) + ages[indx][1], recur(indx+1, lim))


        return recur(0, 0)

