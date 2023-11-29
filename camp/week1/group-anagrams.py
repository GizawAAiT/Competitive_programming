class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for st in strs:
            ky = [0]*26
            for char in st:
                ky[ord(char)-ord("a")] +=1
            res[tuple(ky)].append(st)
        return res.values() 