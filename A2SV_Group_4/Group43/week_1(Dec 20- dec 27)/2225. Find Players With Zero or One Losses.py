class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        dic = {}
        for winner, losser in matches:
            if winner not in dic:
                dic[winner] = [1, 0]
            else: 
                dic[winner][0] +=1
            if losser not in dic:
                dic[losser] = [0, 1]
            else:
                dic[losser][1] +=1
        res = [[],[]]
        for m in matches:
            if dic[m[0]][1] ==0:
                res[0].append(m[0])
            if dic[m[1]][1] ==0:
                res[0].append(m[1])
            if dic[m[0]][1] ==1:
                res[1].append(m[0])
            if dic[m[1]][1] ==1:
                res[1].append(m[1])
        return [sorted(list(set(res[0]))),sorted(list(set(res[1])))]




