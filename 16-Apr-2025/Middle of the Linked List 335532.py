# Problem: Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        slow = fast = head

        # when the fast ptr reachs the end, the slow points to middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow