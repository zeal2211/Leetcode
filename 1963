class Solution:
    def minSwaps(self, s: str) -> int:
        ans = 0
        proper_position = 0
        left, right = 0, len(s) - 1
        s = list(s)

        while left < right:
            if s[left] == '[':
                proper_position += 1
            else:
                proper_position -= 1

            if proper_position < 0:
                while s[right] != '[':
                    right -= 1
                
                s[left], s[right] = s[right], s[left]
                ans += 1
                proper_position += 2
            left += 1

        return ans
