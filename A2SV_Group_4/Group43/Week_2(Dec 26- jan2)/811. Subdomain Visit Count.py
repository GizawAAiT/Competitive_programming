# import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = defaultdict(int)
        for site in cpdomains:
            site = site.split()
            n, site = int(site[0]), '.'+site[1]
            i = 0
            while i<len(site):
                if site[i]=='.':
                    d[site[i+1:]] += n
                i+=1
        return [f'{str(d[i])} {i}' for i in d]
            