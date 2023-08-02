# Middle of the Linked List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
        cnt = 0
        middle = head

        while head:
            head = head.next
            cnt += 1

        i = 0

        while i < cnt // 2:
            i += 1
            middle = middle.next

        return middle


solution = Solution()
solution.middleNode(([1, 2, 3, 4, 5]))
