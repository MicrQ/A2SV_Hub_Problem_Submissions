# Problem: Partition List - https://leetcode.com/problems/partition-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        less = ListNode(float('-inf'))
        high = ListNode(float('inf'))

        curr_less = less
        curr_high = high

        while head:
            if head.val < x:
                curr_less.next = head
                curr_less = curr_less.next

            else:
                curr_high.next = head
                curr_high = curr_high.next

            prev = head
            head = head.next
            prev.next = None

        curr_less.next = high.next

        return less.next