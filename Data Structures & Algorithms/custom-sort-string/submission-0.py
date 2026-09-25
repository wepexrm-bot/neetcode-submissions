class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt_s = Counter(s)
        res =[]

        for ch in order:
            if ch in cnt_s:
                res.append(ch * cnt_s[ch])
                cnt_s[ch] = 0
        
        for ch , freq in cnt_s.items():
            if freq > 0:
                res.append(ch * cnt_s[ch])
        
        return "".join(res)