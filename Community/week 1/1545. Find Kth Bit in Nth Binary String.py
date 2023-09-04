class Solution(object):
    def findKthBit(self, n, k):
        
        sn="0"
        if n==1:
            sn=sn+"0"
        l=0
        d={"0":"1","1":"0"}
        while l<n and len(sn)<k:
            inv_rev=''
            for i in range(len(sn)-1,-1,-1):
                inv_rev=inv_rev+d[sn[i]]
            sn=sn+"1"+inv_rev
            l+=1
        return sn[k-1]
            
            