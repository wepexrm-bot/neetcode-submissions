class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        total = 0
        
        for word in words:
            word_count = Counter(word)
            can_form = True
            for ch , count in word_count.items():
                if count > char_count.get(ch , 0):
                    can_form = False
                    break
                
            if can_form:
                total += len(word)
        return total