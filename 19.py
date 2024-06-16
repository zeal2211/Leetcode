# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c = 0

        def count(head):
            if not head:
                return 0
            return 1 + count(head.next)

        count_list = count(head)
        curr = head
        if count_list - n == 0:
            return head.next

        while curr:
            c += 1
            if count_list - c == n:
                curr.next = curr.next.next
                break
            curr = curr.next

        return head
            
