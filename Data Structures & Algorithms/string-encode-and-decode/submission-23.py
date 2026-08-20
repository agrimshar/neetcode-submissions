class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "dick"
        
        fullString = strs[0]
        print(fullString)

        for c,s in enumerate(strs):
            if c == 0:
                continue
            fullString += "dick" + s
            print(fullString)
        
        return fullString

    def decode(self, s: str) -> List[str]:
        if s == "dick":
            return []
        return s.split("dick")
