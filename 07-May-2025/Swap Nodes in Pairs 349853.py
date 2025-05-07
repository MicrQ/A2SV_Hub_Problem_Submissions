# Problem: Swap Nodes in Pairs - https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(0)
        prev.next = head
        temp = head
        head = prev

        while temp and temp.next:
            prev.next = temp.next
            temp.next = temp.next.next
            prev.next.next = temp

            prev = temp
            temp = temp.next

        return head.next
