class RecentCounter(object):

    def __init__(self):
        self.p=[]        
    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """    
        self.p.append(t)
        c=len(self.p)        
        while self.p[-1]-self.p[0]>3000:
            self.p.pop(0)
            c-=1
        return c
         


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)