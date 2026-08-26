class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minVal = prices[0]
        n = len(prices)

        for i in range(0, n-1):
            if prices[i] > prices[i+1]:
                continue
            
            minVal = min(prices[i], minVal)
            
            j = i + 1
            while j < n and prices[j] >= minVal:
                res = max(res, prices[j] - prices[i])
                j += 1
            
            i = j
        
        return res
