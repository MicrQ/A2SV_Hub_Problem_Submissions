# Problem: Insert a Node at the Tail of a Linked List - https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem

def insertNodeAtTail(head, data):
    node = SinglyLinkedList()
    node.data = data
    node.next = None
    
    if not head:
        return node

    temp = head
    while temp.next:
        temp = temp.next
        
    temp.next = node
    
    return head
