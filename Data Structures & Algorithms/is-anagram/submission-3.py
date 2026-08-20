class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scount = {}
        dcount = {}

        if len(s) != len(t):
            return False

        for i in range(0, len(s)):
            scount[s[i]] = scount.get(s[i], 0) + 1
            dcount[t[i]] = dcount.get(t[i], 0) + 1
        
        if scount == dcount:
            return True
        else:
            return False