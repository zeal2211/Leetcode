class Solution:
    def minLength(self, s: str) -> int:
        stack = [s[0]]

        for char in s[1:]:
            if stack and char == 'B' and stack[-1] == 'A':
                stack.pop()
            elif stack and char == 'D' and stack[-1] == 'C':
                stack.pop()
            else:
                stack.append(char)


        return len(stack)
