class Solution(object):
    def numRescueBoats(self, peo, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        peo = sorted(peo)
        if len(peo)==1:
            return 1
        count = 0
        p1=0
        p2=len(peo)-1
        
        while p1<p2:
            
            if peo[p1]+peo[p2]<=limit and p1!=p2: 
                count +=1
                p1+=1
                p2-=1
           
            else :
                count +=1
                p2-=1
        if p1==p2:
                count +=1
        return count
                
            
                