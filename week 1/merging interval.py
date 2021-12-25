class Solution:
    def merge(self, val:list[list]) -> List[List[int]]:
        val=sorted(val)
        merged=[]
        if len(val)==1:
            return val 
        else:
            
            # escaper=0
            merged.append(val[0])
            for i in range(1,len(val)-1):

                # if escaper==1:
                #     escaper -=1
                #     continue
                # else:    
                if val[i][0]<=merged[len(merged)-1][1] and val[i][0]>=merged[len(merged)-1][0]: 
                    merged[-1]=[min(merged[-1][0],val[i][0]),max(merged[-1][-1],val[i][-1])]
                    # escaper +=1
                else: 
                      merged.append(val[i])
            if merged[-1][-1] < val[-1][0]:
                merged.append(val[-1])
            else:
                merged[-1]=[min(merged[-1][0],val[-1][0]),max(merged[-1][1],val[-1][-1])]
          
            return merged