class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        return len([i for i in count.values()])==len(set([i for i in count.values()]))