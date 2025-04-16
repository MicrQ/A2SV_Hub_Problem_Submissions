# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next:
            return True

        reversedList = None
        temp = head

        # building the revesed version of the list
        while temp:
            reversedList = self.addNodeFront(reversedList, temp.val)
            temp = temp.next

        # comparing the two lists
        while head and reversedList:
            if head.val != reversedList.val:
                return False

            head = head.next
            reversedList = reversedList.next

        return True

    def addNodeFront(self, head: Optional[ListNode], val: int) -> None:
        """ helper """

        node = ListNode(val)
        node.next = head
        head = node

        return head
