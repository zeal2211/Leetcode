class Solution:
    def trap(self, height: List[int]) -> int:

        n = (len(height) - 1)
        dp_right = [0] * len(height)
        dp_left = [0]  * len(height)


        dp_right[0] = height[0]

        for i in range(1, len(height)):
            print(i)
            dp_right[i] = max(height[i], dp_right[i-1])

        dp_left[n] = height[n]

        for i in range(n-1, -1, -1):
            dp_left[i] = max(height[i], dp_left[i+1])

        ans = 0

 
        for i in range(n+1):
            ans += min(dp_left[i], dp_right[i]) - height[i]

        return ans

