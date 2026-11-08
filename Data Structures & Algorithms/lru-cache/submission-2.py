from collections import defaultdict


class ListNode:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next= None
class LRUCache:

    def __init__(self, capacity: int):
        self.limit = capacity
        self.cnt = 0
        self.head = ListNode(0, 0)
        self.back = ListNode(0, 0)
        self.head.next, self.back.prev = self.back, self.head
        self.dict = defaultdict(int)
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    def insert(self, node):
        prev, nxt = self.back.prev, self.back
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
    def get(self, key: int) -> int:
        if key in self.dict:
            self.remove(self.dict[key])
            self.insert(self.dict[key])
            return self.dict[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.remove(self.dict[key])
        self.dict[key] = ListNode(key, value)
        self.insert(self.dict[key])
        if len(self.dict)>self.limit:
            lru = self.head.next
            self.remove(lru)
            del self.dict[lru.key]

