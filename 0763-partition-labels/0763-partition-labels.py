class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for i in range(len(s)): last_index[s[i]] = i
        
        part_size = []
        right_bound = last_index[s[0]]
        i = 0
        size = 1
        while i<len(s):
            right_bound = max(right_bound, last_index[s[i]]) 
            if right_bound == i: 
                part_size.append(size)
                size =1
            else: size +=1
                
            i+=1
        return part_size