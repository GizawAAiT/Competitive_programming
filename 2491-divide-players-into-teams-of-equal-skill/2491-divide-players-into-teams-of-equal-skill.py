class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        res = 0
        one_pair = skill[0]+skill[-1]
        for _ in range(len(skill)//2):
            if skill[_]+skill[-1-_] != one_pair: return -1
            res += skill[_]*skill[-1-_]
        return res