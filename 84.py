class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        stack = [-1]

        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:  
                height = heights[stack.pop()]
                width = i - stack[-1] - 1 
                largest = max(largest, height * width)

            stack.append(i)

        print(largest)
        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = len(heights) - stack[-1] - 1
            largest = max(largest, height * width)

        return largest
