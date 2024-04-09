class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0 
        j = len(s) - 1

        def is_palidrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        while i < j:
            if s[i] != s[j]:
                return is_palidrome(i+1, j) or is_palidrome(i, j-1)
            i += 1
            j -= 1

        return True
