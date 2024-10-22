class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            left, right = i, i

            #Odd length palindrome
            while left >=0 and right < len(s) and s[left] == s[right]:
                currLen = right - left + 1

                if currLen > resLen:
                    resLen = currLen
                    res = s[left: right+1]
                left -= 1
                right += 1
            #Even length palindome

            left, right = i, i + 1

            while left >=0 and right < len(s) and s[left] == s[right]:
                currLen = right - left + 1

                if currLen > resLen:
                    resLen = currLen
                    res = s[left: right+1]

                left -= 1
                right += 1

        return res

