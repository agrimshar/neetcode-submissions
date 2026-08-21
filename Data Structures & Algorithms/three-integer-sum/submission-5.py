class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        nums.sort()
        for i in range(0, len(nums)):
            l, r = i+1, len(nums) - 1
            while l < r:
                temp = nums[i] + nums[l] + nums[r]
                if temp > 0:
                    r -= 1
                elif temp < 0:
                    l += 1
                elif temp == 0:
                    res.add((nums[i], nums[l], nums[r]))
                    r -= 1
                    l += 1
        
        return list(res)

                
