class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = collections.defaultdict(int)
        ans = 0
        left = -1

        for i, char in enumerate(s):
            if char in hashmap:
                left = max(hashmap[char], left)
            hashmap[char] = i
            ans = max(ans, i - left)

        return ans
