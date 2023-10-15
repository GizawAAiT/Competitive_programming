class Solution:
    def countVowels(self, word: str) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        n = len(word)
        answer = 0
        for indx, ch in enumerate(word):
            if ch in vowels:
                answer += (indx+1) * (n-indx)
        return answer
