class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        res = []
        n1, n2 = len(word1), len(word2)
        i, j = 0, 0
        while i < n1 and j < n2:
            if word1[i:] > word2[j:]:
                res.append(word1[i])
                i += 1
            else:
                res.append(word2[j])
                j += 1
        res += word1[i:]
        res += word2[j:]
        return ''.join(res)