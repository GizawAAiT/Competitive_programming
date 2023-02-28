class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.steam_count = 0
    def consec(self, num: int) -> bool:
        if num == self.value:
            self.steam_count += 1
        else:
            self.steam_count = 0
        return self.steam_count >= self.k

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)