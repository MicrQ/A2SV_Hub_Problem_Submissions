# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        reminder = 0
        results = []

        while l1 or l2:

            result = 0
            if l1:
                result += l1.val
                l1 = l1.next
            if l2:
                result += l2.val
                l2 = l2.next

            result += reminder

            reminder = result // 10
            result %= 10
            results.append(result)

        if reminder != 0:
            results.append(reminder)

        return self.listBuilder(results)

    def listBuilder(self, nums: List[int]) -> Optional[ListNode]:
        """ builds a linked list from a list of ints """

        if not nums:
            return None


        head = None
        for i in range(len(nums) - 1, -1, -1):

            node = ListNode(nums[i])
            node.next = head
            head = node

        return head
