from collections import defaultdict
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        dic = defaultdict(int)
        lead = self.persons[0]
        dic[lead] += 1
        for i in range(1, len(self.persons)):
            dic[self.persons[i]] += 1
            if dic[self.persons[i]] >= dic[lead]:
                lead = self.persons[i]
            self.persons[i] = lead
            
        self.times = times
        

    def q(self, t: int) -> int:
        left = -1
        right = len(self.times)
        while left < right-1:
            mid = left + (right - left)//2
            
            if self.times[mid] <= t:
                left = mid
            else: 
                right = mid
        return self.persons[left] 


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)