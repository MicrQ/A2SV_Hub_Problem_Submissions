# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        slow = fast = head
        max_sum = float('-inf')

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # building the reversed version of the right half of the list
        new_list = self.listReverser(slow)

        temp = head
        while new_list:
            sum_ = temp.val + new_list.val
            max_sum = max(max_sum, sum_)

            new_list = new_list.next
            temp = temp.next

        return max_sum
        
    def listReverser(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ builds the reversed version of a linked list from given linked list """

        prev = None

        while head.next:
            next_ = head.next
            head.next = prev
            prev = head
            head = next_

        head.next = prev

        return head
