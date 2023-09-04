class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pref = [0 for _ in range(1002)]
        for t in trips:
            pref[t[1]] += t[0]
            pref[t[2]] -= t[0]
        if pref[0] > capacity: return False
        for i in range(1, len(pref)):
            pref[i] += pref[i-1]
            if pref[i] > capacity: return False
        return True
         