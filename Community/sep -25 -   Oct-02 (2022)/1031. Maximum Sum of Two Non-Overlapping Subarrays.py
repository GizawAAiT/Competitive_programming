class Solution:
    def maxSumTwoNoOverlap(self, n: List[int], f: int, s: int) -> int:
        for i in range(1,len(n)): n[i]+=n[i-1]
        res = 0
        for i in range(f-1,len(n)):
            sum1 = n[i] if f-1==i else n[i]-n[i-f]
            if i-f >= s-1:
                for j in range(s-1, i-f+1):
                    sum2 = n[j] if s-1 ==j else n[j]-n[j-s]
                    res = max(res, sum1+sum2)
                    # print("back",(i,j),"+++>","sums",(sum1,sum2),res)
            for j in range(i+s, len(n)):
                sum2 = n[j]-n[j-s]
                res = max(res, sum1+sum2)
                # print("front",(i,j),"+++>","sums",(sum1,sum2),res)
        return res