class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        fl_group = defaultdict(list)
        
        for s in paths:
            s = s.split()
            for i in range(1,len(s)):
                fl_name, content = s[i].split('(')
                content = content[:-1]
                
                fl_group[content].append('/'.join([s[0],fl_name]))
        res = []
        for content in fl_group:
            if len(fl_group[content])>1:
                res.append(fl_group[content])
        return res
