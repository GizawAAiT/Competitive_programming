class MyQueue(object):

    def __init__(self):
        self.st1=[]
        self.st2=[]


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.st1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        while self.st1:
            self.st2.append( self.st1.pop() )
        
        x=self.st2.pop()
        
        while self.st2:
            self.st1.append( self.st2.pop() )
        return x

    def peek(self):
        """
        :rtype: int
        """
        while self.st1:
            self.st2.append(self.st1.pop())
        x=self.st2[-1]
    
       
        while self.st2:
            self.st1.append( self.st2.pop() )
        
        return x


    def empty(self):
        """
        :rtype: bool
        """
        return not (self.st1 or self.st2)
        

