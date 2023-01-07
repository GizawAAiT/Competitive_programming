class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        pref =[0]
        suf = [0]
        l, r = int(boxes[0]),int(boxes[-1])
        
        for i in range(1,len(boxes)):
            pref.append(pref[-1]+l)
            suf.append(suf[-1]+r)
            l += int(boxes[i])
            r += int(boxes[-1-i]) 
            
        return [pref[i]+suf[-1-i] for i in range( len(boxes))]