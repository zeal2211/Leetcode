class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [-1] * 26
        last = [-1] * 26
        ans = 0

        for i in range(len(s)):
            val = ord(s[i]) - ord('a')
            if first[val] == -1:
                first[val] = i
            last[val] = i

        for i in range(26):
            if first[i] == -1:
                continue
            between = set()
            for j in range(first[i]+1, last[i]):
                between.add(s[j])

            ans += len(between)

        return ans
