class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        ans, mid = 0, False

        for word in count:
            rev = word[1] + word[0]
            if rev == word:
                ans += 4 * (count[word]//2)
                mid = mid or count[word]%2 == 1
            
            else:
                ans += 2 * min(count[word], count[rev])
        return ans + 2 if mid else ans
            

            



