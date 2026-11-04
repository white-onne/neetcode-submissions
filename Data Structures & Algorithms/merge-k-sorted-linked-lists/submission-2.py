# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        for lst in lists:
            cur = lst
            while cur:
                heapq.heappush(pq, cur.val)
                cur = cur.next
        new_node = ListNode()
        head = new_node
        while pq:
            val = heapq.heappop(pq)
            node = ListNode(val)
            new_node.next = node
            new_node = new_node.next
        return head.next