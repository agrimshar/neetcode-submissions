class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        t_count, s_count = {}, {}

        for i in range(len(s)):
            t_count[t[i]] = 1 + t_count.get(t[i], 0)
            s_count[s[i]] = 1 + s_count.get(s[i], 0)
        return t_count == s_count

        