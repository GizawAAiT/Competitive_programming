class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.st = []
    def push(self, x: int) -> None:
        if len(self.st) < self.maxSize: 
            self.st.append(x)

    def pop(self) -> int:
        return self.st.pop() if self.st else -1

    def increment(self, k: int, val: int) -> None:
        i = 0
        while i<len(self.st) and i<k:
            self.st[i]+=val
            i+=1


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)