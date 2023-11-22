class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.left = 0
        self.queue = []

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.queue.append(value)
            return True
        # return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            # res = self.quequ[self.left]
            self.left += 1
            return True
        
    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[self.left]    
        return -1
    def Rear(self) -> int:
        if not self.isEmpty():
            return self.queue[len(self.queue)-1] 
        return -1

    def isEmpty(self) -> bool:
        return len(self.queue) - self.left == 0 

    def isFull(self) -> bool:
        return len(self.queue) - self.left == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()