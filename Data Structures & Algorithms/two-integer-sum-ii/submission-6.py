class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []

        l, r = 0, len(numbers) - 1

        while l < r:
            cur = numbers[l] + numbers[r]
            if cur > target:
                r -= 1
                continue
            if cur < target:
                l += 1
                continue
            return [l + 1, r + 1]
        
        return []