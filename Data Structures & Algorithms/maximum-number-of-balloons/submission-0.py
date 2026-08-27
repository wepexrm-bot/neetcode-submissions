class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        word = Counter("balloon")
        res = len(text)

        for c in word:
            res = min(res , count[c] // word[c])
        return res