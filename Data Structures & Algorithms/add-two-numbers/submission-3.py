# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 리스트를 만들고 연결하는 방법
        node = ListNode()
        node.next = ListNode()
        node = node.next
        
        # 여기서부터 시작
        num = 0
        dummy = ListNode(0)
        node = dummy

        while l1 and l2:
            num += (l1.val + l2.val)
            if num > 9:
                node.next = ListNode(num - 10)
                num = 1
            else:
                node.next = ListNode(num)
                num = 0
            node = node.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            num += l1.val
            if num > 9:
                node.next = ListNode(num - 10)
                num = 1
            else:
                node.next = ListNode(num)
                num = 0
            node = node.next
            l1 = l1.next

        while l2:
            num += l2.val
            if num > 9:
                node.next = ListNode(num - 10)
                num = 1
            else:
                node.next = ListNode(num)
                num = 0
            node = node.next
            l2 = l2.next
        
        if num != 0:
            node.next = ListNode(num)

        return dummy.next