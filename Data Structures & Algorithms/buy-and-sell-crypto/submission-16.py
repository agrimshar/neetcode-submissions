class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = prices[0]
        res = 0

        for price in prices[1:]:
            res = max(res, price - minVal)
            minVal = min(minVal, price)

        return res
