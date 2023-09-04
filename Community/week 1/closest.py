class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d={}
        answer=[]
        l=[]
        for p in points:
            s= int((float("{:.5f}".format(sqrt(p[0]**2+p[1]**2)))*10000)//1)
            d[s] = p
            l.append(s)
        for i in range(len(l)):
            for j in range(i,len(l)):
                if l[i]>l[j]:
                    l[i],l[j]=l[j],l[i]
        l=l[:k]
        for i in range(k):
            answer.append(d[l[i]])
        return answer