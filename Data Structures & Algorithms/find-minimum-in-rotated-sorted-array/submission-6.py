class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        m = l + ((r - l) // 2)
        res = min(nums[l], nums[r])

        while l <= r:
            if nums[m] < res:
                res = nums[m]
                r = m - 1
            else:
                l = m + 1
            
            m = l + ((r - l) // 2)
        
        return res
