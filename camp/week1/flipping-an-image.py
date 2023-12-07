class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        def invert_flip(arr):
            return [1 if x == 0 else 0 for x in arr[::-1]]
        
        for i in range(len(image)):
            image[i] = invert_flip(image[i])
        
        return image