# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        stack_l1 = []
        stack_l2 = []

        while l1:
            stack_l1.append(l1.val)
            l1 = l1.next

        while l2:
            stack_l2.append(l2.val)
            l2 = l2.next

        head = None
        reminder = 0
        while stack_l1 or stack_l2:
            sum_ = reminder

            if stack_l1:
                sum_ += stack_l1.pop()

            if stack_l2:
                sum_ += stack_l2.pop()

            reminder = sum_ // 10
            node = ListNode(sum_ % 10)
            node.next = head
            head = node

        if reminder != 0:
            node = ListNode(reminder)
            node.next = head
            head = node

        return head
