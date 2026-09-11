class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_str = defaultdict(int)
        pair = 0
        for w in s:
            count_str[w] += 1

        has_odd = False
        for ch in count_str:
            pair += count_str[ch] // 2         
            if count_str[ch] % 2 == 1:           
                has_odd = True
        
        return (pair * 2) + (1 if has_odd else 0)