# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visit_node = set()

        while head:
            if head in visit_node:
                return True
            else:
                visit_node.add(head)
                head = head.next
        return False
        