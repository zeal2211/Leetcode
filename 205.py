class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}

        for i in range(len(s)):
            if s[i] in hashmap1:
                if hashmap1[s[i]] != t[i]:
                    return False
            else:
                hashmap1[s[i]] = t[i]
                
            if t[i] in hashmap2:
                if hashmap2[t[i]] != s[i]:
                    return False
            else:
                hashmap2[t[i]] = s[i]

        return True
