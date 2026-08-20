class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "nigger1"
        return "nigger".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "nigger1":
            return []
        return s.split("nigger")
