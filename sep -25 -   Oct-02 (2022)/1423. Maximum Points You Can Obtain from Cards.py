class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        window = len(cardPoints)-k
        cur_sum = min_sum = sum(cardPoints[:window])
        
        i, j = 0, window
        while j<len(cardPoints):
            cur_sum +=cardPoints[j]-cardPoints[i]
            i, j= i+1, j+1
            min_sum = min(min_sum,cur_sum)
        return sum(cardPoints)-min_sum