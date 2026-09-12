class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_s = Counter(s)
        for i ,  c in enumerate(s):
            if count_s[c] == 1:
                return i
        
        return -1