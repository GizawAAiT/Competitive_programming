class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        left =[0]
        right = [0]
        l, r = int(boxes[0]),int(boxes[-1])
        
        for i in range(1,len(boxes)):
            left.append(left[-1]+l)
            right.append(right[-1]+r)
            l += int(boxes[i])
            r += int(boxes[-1-i]) 
        return [left[i]+right[-1-i] for i in range( len(boxes))]