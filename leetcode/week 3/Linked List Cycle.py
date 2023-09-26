# Linked List Cycle
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodes = []
        
        while head:
            if head in nodes:
                return True
            else:
                nodes.append(head)
            head = head.next        
        
        return False
