class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_list = list(s)

        for c in t:
            if c in char_list:
                char_list.remove(c)
            else:
                return False
        
        return True
        

        