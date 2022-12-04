class Solution:
    def isHappy(self, n: int) -> bool:
        if n ==1:
            return True
        
        def fact(n):
            s = 0
            while n > 9:
                s += (n%10) **2
                n = n//10
            s += n**2
            return s
        collection = set() 
        collection.add(n)
        while True:            
            n = fact(n)
            if n in collection:
                return n ==1
            collection.add(n)
        
