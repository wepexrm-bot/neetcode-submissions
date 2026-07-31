class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i,j= 0, 0
        while i < len(s) and j < len(t):
            if t[j] == s[i]:
                j += 1
            i += 1
        
        if j != len(t):
            sub = t[j::]
            s += sub
            return len(sub)
        else:
            return 0