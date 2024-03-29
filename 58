class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s) - 1
        output = 0
        flag = True

        while n > -1:
            if s[n] != ' ':
                flag = False
            if s[n] == ' ' and not flag:
                break
            n -= 1    
            if not flag:
                output += 1

        return output
