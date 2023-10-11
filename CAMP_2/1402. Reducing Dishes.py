class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse = True)
        # print(satisfaction)
        total = maximum = 0
        indx = 0
        while indx < len(satisfaction):
            if total < -satisfaction[indx]:
                return maximum
            
            maximum += total + satisfaction[indx]
            total += satisfaction[indx]
            
            indx += 1
        return maximum
            
