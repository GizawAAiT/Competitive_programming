class Solution:
    def maxSumOfThreeSubarrays(self, n: List[int], k: int) -> List[int]:
        print(n)
        w = [sum(n[:k])]
        for i in range(k,len(n)): 
            w.append(w[-1]+(n[i]-n[i-k]))
        print(w)
        l, r = 0, len(w)-1
        left_max, right_max = [], []
        for i in range(len(w)):
            if w[i] > w[l]:
                l = i
            if w[len(w)-i-1] >= w[r]:
                r = len(w)-i-1
            left_max.append(l)
            right_max.insert(0,r)
        
        res = []
        max_sum = 0
        for m in range(k,len(w)-k):
            l, r = left_max[m-k], right_max[m+k]
            s = w[l] + w[m] + w[r]
            if s > max_sum:
                max_sum = s
                res = [l, m, r]
        return res