class Solution:
    def candy(self, ratings: List[int]) -> int:
        left_max = [1]
        right_max = [1]
        for _ in range(1,len(ratings)):
            if ratings[_-1] < ratings[_]: 
                left_max.append(left_max[-1]+1)
            else: left_max.append(1)
            
            if ratings[-_] < ratings[-1-_]: 
                right_max.append(right_max[-1]+1)
            else: right_max.append(1)
        right_max.reverse()
        print(left_max, right_max)  
        return sum([max(right_max[_], left_max[_]) for _ in range(len(ratings))])