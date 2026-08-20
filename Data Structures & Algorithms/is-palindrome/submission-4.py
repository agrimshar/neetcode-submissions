class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = True
        chars = s.lower()

        l, r = 0, len(s)-1
        while l < r:
            if not chars[l].isalnum():
                l += 1
                continue
            if not chars[r].isalnum():
                r -= 1
                continue
            
            if chars[l] != chars[r]:
                return False
            
            l += 1
            r -= 1
        
        return res