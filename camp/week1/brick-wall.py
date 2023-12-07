class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        breaking_points = defaultdict(int)
        max_breaking = 0
        for w in wall:
            i = 0
            for width in w[:-1]:
                i += width
                breaking_points[i] += 1
                max_breaking = max(max_breaking, breaking_points[i])
        
        return len(wall)-max_breaking

