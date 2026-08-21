class Solution:
    def maxDifference(self, s: str) -> int:
        count = {}
        for char in s:
            count[char] = 1 + count.get(char, 0)
        
        maxodd = 0
        mineven = float('inf')
        
        for freq in count.values():
            if freq % 2 == 0:
                mineven = min(mineven, freq)
            else:
                maxodd = max(maxodd, freq)
        
        return maxodd - mineven