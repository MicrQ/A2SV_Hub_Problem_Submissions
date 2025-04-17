# Problem: Remove Duplicates from Sorted List - https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        temp = head
        while temp.next:

            # checking if the current and the next node have same val
            if temp.val == temp.next.val:
                dlt = temp.next
                temp.next = temp.next.next
                dlt.next = None

            else:
                temp = temp.next

        return head