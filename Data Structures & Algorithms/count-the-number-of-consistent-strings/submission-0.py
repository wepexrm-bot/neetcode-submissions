class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            is_valid = True
            for ch in word:
                if ch not in allowed:
                    is_valid = False
                    break
            if is_valid:        
                count += 1
        return count