class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_cnt = Counter(ransomNote)
        magazine_cnt = Counter(magazine)
        for ch in ransomNote_cnt:
            if magazine_cnt[ch] < ransomNote_cnt[ch]:
                return False
        return True


