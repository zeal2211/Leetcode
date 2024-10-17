class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            # print(stack)
            if char == ']':
                curr_string = []
                while stack[-1] != '[':
                    curr_string.insert(0, stack.pop())

                num = []
                stack.pop()

                while stack and stack[-1].isdigit():
                    num.insert(0, stack.pop())
                
                for i in range(int(''.join(num))):
                    stack += curr_string
            else:
                stack.append(char)

        
        return ''.join(stack)
