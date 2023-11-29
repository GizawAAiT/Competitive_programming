class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        intVal = {"A":1, "C": 2, "G": 3, "T":4}
        def addFront(hash_val, i, j):
            return hash_val + (intVal[s[j]] * pow(4, j-i)) 
        
        def dropBack(hash_val, i, j):
            return (hash_val - (intVal[s[i]]))//4
        
        hash_val, count, ans = 0, defaultdict(int), []
        i, j = 0, 0
        
        while j < len(s):
            hash_val = addFront(hash_val, i, j)
            if j-i >= 10:
                hash_val = dropBack(hash_val, i, j)
                i += 1
 
            j += 1
            
            # update the count:
            count[hash_val] += 1

            # update the answer:
            if count[hash_val] == 2:
                ans.append(s[i:j])
            
        return ans




            
        
