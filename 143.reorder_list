# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []

        curr = head

        while curr:
            stack.append(curr.val)
            curr = curr.next

        curr = head
        i = 0 
        j = len(stack) - 1
        flag = True

        print(stack)
        while i <= j:
            if flag:
                curr.val = stack[i]
                i += 1
                flag = False
            else:
                curr.val = stack[j]
                j -= 1
                flag = True
            curr = curr.next

        return head
