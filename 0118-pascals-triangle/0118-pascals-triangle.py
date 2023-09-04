class Solution:
    def generate(self, R: int) -> List[List[int]]:
        pascal = [[1]]
        for _ in range(R-1):
            t = [1]
            for i in range(len(pascal[-1])-1):
                t.append(pascal[-1][i] + pascal[-1][i+1])
            t.append(1)
            pascal.append(t)
        return pascal