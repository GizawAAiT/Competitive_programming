class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        root = [i for i in range(26)]
    
        def getRoot(x):
            if root[x] == x:
                return x
            root[x] = getRoot(root[x])
            return root[x]
        
        def merge(x, y):
            root_x, root_y = getRoot(x), getRoot(y)
            if root_x != root_y:
                if root_x < root_y:
                    root[root_y] = root_x
                else:
                    root[root_x] = root_y
        
        for a, b in zip(s1, s2):
            x, y = ord(a)- ord('a'), ord(b)- ord('a')
            merge(x, y)
        # print(root)
        answer = ''
        for char in baseStr:
            answer += chr(getRoot(ord(char)-ord('a')) + ord('a'))

        return answer

            

        

