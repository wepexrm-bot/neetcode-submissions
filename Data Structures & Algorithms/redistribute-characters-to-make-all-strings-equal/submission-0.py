class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        ch_word = defaultdict(int)

        for i in words:
            for c in i:
                ch_word[c] += 1

        for ch in ch_word:
            if ch_word[ch] % len(words):
                return False
        return True