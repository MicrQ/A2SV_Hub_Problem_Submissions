# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        parts = []
        nodes = 0

        # counting number of nodes
        temp = head
        while temp:
            nodes += 1
            temp = temp.next

        # nodes in one part of the linked list
        part_len = nodes // k
        leftover = nodes % k
        temp = head

        for _ in range(k):

            curr_head = temp
            part_size = part_len + (1 if leftover > 0 else 0)
            leftover -= 1

            # moving to the end of the partition
            for _ in range(part_size - 1):
                if temp:
                    temp = temp.next

            # cutting the partition
            if temp:
                next_head = temp.next
                temp.next = None
                temp = next_head
                parts.append(curr_head)

            else:
                parts.append(None)

        return parts