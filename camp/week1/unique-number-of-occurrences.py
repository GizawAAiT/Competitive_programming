class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        for repetition in Counter(list(count.values())).values():
            print(repetition)
            print(list(count.values()))
            if repetition > 1: return False

        return True