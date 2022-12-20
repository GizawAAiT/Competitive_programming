class Solution:
    def average(self, salary: List[int]) -> float:
        minimum, maximum = salary[0], salary[0]
        total = 0
        for s in salary:
            if s < minimum:  
                minimum = s
            elif s > maximum:
                maximum = s
            total += s
        return ((total - minimum - maximum )/ (len(salary)-2))
        