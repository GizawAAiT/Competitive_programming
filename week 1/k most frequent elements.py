class Solution(object):
    def topKFrequent(self, n, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(n)==1:
            return n
        n=sorted(n)
        d={}
        i=0
        c=1
        a=[]
        d[n[i]]=c
        while i<len(n)-1:
            i+=1
            if n[i]==n[i-1]:
                c+=1
            else:
                d[n[i-1]]=c
                c=1
        
            
        d[n[-1]]=c
        bl=len(d.keys())
        bu=[]
        for i in range(bl+1):
            
            bu.append([])
        keys=d.keys()
        if len(keys)==1:
            return keys
        bu=list(bu)
        for i in keys: 
            bu[d[i]].append(i) 
        p=1
        s=0
        while s<k:
            a.append(bu[-p])
            s+=len(bu[-p])
            p+=1
            
        a=list(a)
        an=[]
        for i in a:
            an.extend(i)
        return an
    
            
        
            
        
       
        