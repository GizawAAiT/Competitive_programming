class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n == 1: 
            return [[1]]
        pas = [[1]]
        pas.append([1,1])
        print(pas)
        i = 2
        while i < n:
            pas.append([1,1]) 
            j = 1
            while j < i:
                print(f"pas[i] : {pas[i]}") 
                pas[i].insert(j,(pas[i-1][j-1]+pas[i-1][j]))
                j+=1
            i+=1
        return pas          
           
        print(pas)