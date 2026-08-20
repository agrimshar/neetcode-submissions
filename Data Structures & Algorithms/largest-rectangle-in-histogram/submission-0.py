class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            start = i 
            
            while stack and h < stack[-1][0]:
                height, index = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            
            stack.append((h, start))
            
        
        return maxArea