class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]
        
        ans: List[List[str]] = []
        groups = {}
        ans_index = 0

        for i, s in enumerate(strs):
            sorted_string = "".join(sorted(s))

            if sorted_string not in groups:
                groups[sorted_string] = ans_index
                ans.append([s])
                ans_index += 1
            else:
                ans[groups[sorted_string]].append(s)
        return ans
        