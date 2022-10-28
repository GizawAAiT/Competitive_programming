class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        dic = {}
        for arr in nums: 
            for n in arr:
                if n in dic.keys():
                    dic[n] += 1
                else: dic[n] = 1
        
        res, N = [], len(nums)
        for n in dic.keys():
            if dic[n]== N: res.append(n)
        res.sort()
        return res