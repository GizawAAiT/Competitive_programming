
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        eulerGraph = defaultdict(list)
       
        for u, v in tickets:
            eulerGraph[u].append(v)
        
        for dest in eulerGraph.values():
            dest.sort(reverse = True)

        res = []
        def dfsEuler(root):
            destinations = eulerGraph[root]

            # Visit destinations in lexical order
            while destinations:
                next_destination = destinations.pop()
                dfsEuler(next_destination)

            res.append(root)

        dfsEuler('JFK')
        return list(reversed(res))

