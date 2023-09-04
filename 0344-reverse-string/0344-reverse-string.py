class Solution:
    def reverseString(self, s: List[str], l=0) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if l>=len(s)//2:
            return
        s[l], s[-1-l] = s[-1-l], s[l]
        self.reverseString(s, l+1)
            