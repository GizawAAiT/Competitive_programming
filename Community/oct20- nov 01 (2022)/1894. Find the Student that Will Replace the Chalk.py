class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        
        i, l = 0, len(chalk)
        s = sum(chalk)
        k = k%s 
        while k>=chalk[i]:
            k -= chalk[i]
            i = (i+1)%l
        return i