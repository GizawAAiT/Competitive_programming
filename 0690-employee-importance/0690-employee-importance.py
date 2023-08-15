"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mapping = { em.id : (em.importance, em.subordinates) for em in employees}
        
        que = [id]
        result = 0
        def update_que(indx):
            for id in mapping[indx][1]: 
                que.append(id)
        while que:
            indx = que.pop()
            update_que(indx)
            result += mapping[indx][0] 
        return result
