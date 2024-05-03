class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        left = 0
        right = 0

        while right < len(haystack):
            while right < len(haystack) and haystack[right] == needle[right - left]:
                if right - left == len(needle) - 1:
                    return left
                right += 1
            left += 1
            right = left

        return -1
                
