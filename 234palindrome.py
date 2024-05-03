# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        stack = []

        while curr:
            stack.append(curr.val)
            curr = curr.next

        i = 0
        j = len(stack) - 1

        while i < j:
            if stack[i] != stack[j]:
                return False
            i += 1
            j -= 1

        return True
