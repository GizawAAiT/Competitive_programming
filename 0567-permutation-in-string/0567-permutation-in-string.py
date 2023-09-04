class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic_1 = Counter(s1)
        def compare(dic_2):
            for k in dic_1:
                if dic_1[k] != dic_2[k]: return False
            return True
        
        left = 0
        dic_2 = defaultdict(int)
        for right in range(len(s2)):
            dic_2[s2[right]] += 1
            while right-left+1 > len(s1):
                dic_2[s2[left]] -=1
                left +=1
            if right -left +1>=len(s1) and compare(dic_2):
                return True
        return False