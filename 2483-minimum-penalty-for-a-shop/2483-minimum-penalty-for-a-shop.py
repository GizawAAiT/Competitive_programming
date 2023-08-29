class Solution:
    def bestClosingTime(self, customers: str) -> int:
        customers += "z"
        min_cost = len(customers)
        count = Counter(customers)
        Y = 0
        N = 0
        ans = 0
        for i in range(len(customers)):
            cost = N + (count["Y"]-Y)
            if min_cost > cost:
                min_cost = cost
                ans = i
           
            #UPDATE    
            Y += customers[i] == "Y"
            N += customers[i] == "N"
            
        return ans