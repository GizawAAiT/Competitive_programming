class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = [-1]
        
        for i in range(len(arr)-1, 0, -1):
            greatest.append(max(greatest[-1],arr[i])) 
        return reversed(greatest)