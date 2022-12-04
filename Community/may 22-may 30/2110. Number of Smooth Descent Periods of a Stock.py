class Solution(object):
    def getDescentPeriods(self, prices):
        
        A=len(prices)
        
        count=1.0
        for i in range(1,len(prices)):
            if prices[i]==prices[i-1]-1:
                count+=1
            else:
                
                A+=((count/2.0)*(count-1)) 
                count=1
        A+=((count/2.0)*(count-1))
        return int(A)
