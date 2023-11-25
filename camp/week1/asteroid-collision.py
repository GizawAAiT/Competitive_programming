class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for ast in asteroids:
            while ast < 0:
                if not st or st[-1] < 0:
                    st.append(ast)
                    ast = 0
                
                elif st[-1] < -ast:
                    st.pop()
                elif st[-1] > -ast:
                    ast = 0
                else:
                    st.pop()
                    ast = 0
            if ast:
                st.append(ast)
                
        return st


