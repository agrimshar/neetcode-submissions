class Solution:
    def isValid(self, s: str) -> bool:
        arrLen = len(s)
        if arrLen % 2 == 1: return False
        if arrLen == 0: return True

        stack = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
                continue
            
            if len(stack) == 0:
                return False
            
            if c == ")" and stack.pop() != "(":
                return False
            
            if c == "]" and stack.pop() != "[":
                return False
            
            if c == "}" and stack.pop() != "{":
                return False
        
        return len(stack) == 0