class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.k = k
        self.que = [None] * k
        self.fr = self.re = -1
        

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.re==(self.fr+1)%self.k:
            return False
        else:
            if self.fr==-1:
                self.re=self.fr=0
            else:
                self.fr=(self.fr+1)%self.k
            self.que[self.fr]=value
        return True
        
        
    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.re==(self.fr+1)%self.k:
            return False
        else:
            if self.re==-1:                
                self.fr=self.re=self.k-1
            else:
                if self.re==0:
                    self.re=self.k-1
                else:
                    self.re-=1
            self.que[self.re]=value
        return True

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.fr==-1:
            return False
        elif self.re==self.fr:
            self.que[self.fr]=None
            self.re=self.fr=-1
        else:
            self.que[self.fr]=None
            if self.fr==0:
                self.fr=self.k-1
            else:                
                self.fr-=1
        return True

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.re==-1: 
            return False
        elif self.re==self.fr:
            self.que[self.fr]=None
            self.re=self.fr=-1
        else:
            self.que[self.re]=None
            self.re=(self.re+1)%self.k
        return True

    def getFront(self):
        """
        :rtype: int
        """
        if self.fr==-1:
            return -1
        return self.que[self.fr]

    def getRear(self):
        """
        :rtype: int
        """
        
        if self.re==-1:
            return -1
        return self.que[self.re]

    def isEmpty(self):
        """
        :rtype: bool
        """
        if self.fr==-1:
            return True
        return False

    def isFull(self):
        """
        :rtype: bool
        """
        if (self.fr+1)%self.k==self.re and self.fr!=-1:
            return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()