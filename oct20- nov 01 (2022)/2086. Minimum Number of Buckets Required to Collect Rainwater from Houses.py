class Solution:
    def minimumBuckets(self, street: str) -> int:
        street = list(street)
        b = 0
        for i in range(len(street)):
            if street[i]=='H': 
                if i>0 and i<len(street)-1 and street[i-1]=="H" and street[i+1]=="H" or (i==0 and (len(street) == 1 or street[1]=="H")) or i == len(street)-1 and street[i-1] =="H":
                    return -1
                
                elif street[i-1] =="B": 
                    b += 0
                elif i+1 < len(street)  and street[i+1]==".": 
                    street[i+1]="B"
                    b+=1
                else: 
                    b+=1
        return b