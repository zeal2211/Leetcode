class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0 

        freq = collections.defaultdict(int)
        max_freq = 0
        longest_substring = 0
        
        for end in range(len(s)):
            freq[s[end]] += 1

            max_freq = max(max_freq, freq[s[end]])

            if not (end - start + 1 - max_freq <= k):
                freq[s[start]] -= 1
                start += 1

            longest_substring = max(longest_substring, end + 1 - start)


        return longest_substring
