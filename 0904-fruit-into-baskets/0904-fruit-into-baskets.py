class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic = defaultdict(int)
        left = 0
        mx = 0
        for right in range(len(fruits)):
            dic[fruits[right]]+=1
            while left < right and  len(dic) > 2:
                dic[fruits[left]] -=1 
                
                if dic[fruits[left]] == 0:
                    del dic[fruits[left]]
                left += 1
            if len(dic) < 3:
                mx = max(mx, right-left+1)
            
        return mx