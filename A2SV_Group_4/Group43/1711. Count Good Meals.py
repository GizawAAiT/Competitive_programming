class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        powers = [2**n for n in range(22)]
        
        # create and build a frequency dictionary
        dic = {}
        for d in deliciousness:
            if d in dic:
                dic[d] += 1
            else:
                dic[d] = 1
        pairs = 0
        # iterate over the dictionary 
        for n in dic.keys():
            for p in powers:
                diff = p - n
                if diff in dic and diff == n:
                    pairs += (dic[n]*(dic[n]-1))
                    # print((n, diff))
                elif diff in dic:
                    pairs += dic[n]*dic[diff]
                    # print((n, diff))
        return (pairs//2)%(10**9 + 7)