class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        if len(s) != len(pattern):
            return False

        hashmap1 = {}
        hashmap2 = {}

        for i, char in enumerate(pattern):
            if char in hashmap1:
                if hashmap1[char] != s[i]:
                    return False
            else:
                hashmap1[char] = s[i]
            if s[i] in hashmap2:
                if hashmap2[s[i]] != char:
                    return False
            else:
                hashmap2[s[i]] = char

        return True
