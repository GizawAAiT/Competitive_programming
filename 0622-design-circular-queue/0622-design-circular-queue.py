class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.length = 0
        self.tail = self.head = Node()
        

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            if self.isEmpty():
                self.head = self.tail = Node(value)  
            else:
                self.tail.next = Node(value)
                self.tail = self.tail.next
            self.length += 1
            return True
        # return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.head = self.head.next
            self.length -= 1
            return True 
        
    def Front(self) -> int:
        if not self.isEmpty():
            return self.head.val   
        return -1
    def Rear(self) -> int:
        if not self.isEmpty():
            return self.tail.val  
        return -1
    def isEmpty(self) -> bool:
        return self.length == 0 

    def isFull(self) -> bool:
        return self.length == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()