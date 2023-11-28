from sortedcontainers import SortedList
class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, v: str, t: int) -> None: 
        if key not in self.dic:
            self.dic[key] = SortedList()
        self.dic[key].add((t, v))

    def get(self, key: str, t: int) -> str:
        if key not in self.dic: return ''
        l, r = -1, len(self.dic[key])
        while l<r-1:
            mid = l + (r-l)//2
            if self.dic[key][mid][0] <= t:
                l = mid
            else: r = mid
        
        return self.dic[key][l][1] if l >= 0 else ''
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)