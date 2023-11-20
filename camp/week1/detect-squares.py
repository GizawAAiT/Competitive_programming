class DetectSquares:

    def __init__(self):
        self.freq = defaultdict(int)        

    def add(self, point: List[int]) -> None:
        self.freq[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x0, y0 = point
        res = 0
        for x, y in self.freq.copy():
            slop = (y-y0)/(x-x0) if (x-x0) != 0 else 0
            if slop in [1,  -1]:
                res += self.freq[(x, y0)] * self.freq[(x0, y)] * self.freq[(x, y)]
                
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)