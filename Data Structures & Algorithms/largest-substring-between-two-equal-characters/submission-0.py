class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = 0
        hasequal = False
        for i in range(len(s)):
            for j in range( len(s)-1, i , -1):
                if s[i] == s[j]:
                    hasequal = True
                    res = max(res , len(s[ i+1 : j]))
                

        return res if hasequal else -1