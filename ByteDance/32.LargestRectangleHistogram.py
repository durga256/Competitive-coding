class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [[0,heights[0]]]; maxArea = heights[0]
        for i in range(1,len(heights)):
            if heights[i] < stack[-1][1]:
                while len(stack) > 0 and stack[-1][1] > heights[i]:
                    maxArea = max(maxArea, stack[-1][1]*(i-stack[-1][0]))
                    popped_last_idx = stack[-1][0]
                    stack.pop()
                stack.append([popped_last_idx,heights[i]])
            else:
                stack.append([i, heights[i]])

        n = len(heights)
        #to handle indexes that werent popped
        for i in range(len(stack)):
            maxArea = max(maxArea, stack[i][1]*(n-stack[i][0]))

        return maxArea