# Reverse Linked List

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    prev = None
    curr = head
    nxt = head.next
    while nxt:
        curr.next = prev
        prev = curr
        curr = nxt
        nxt = nxt.next
    curr.next = prev
    return curr

def printLinkedList(head: ListNode):
    if head:
        print(head.val)
        printLinkedList(head.next)
    return


node3 = ListNode(val= 3)
node2 = ListNode(val= 2, next= node3)
node1 = ListNode(val= 1, next= node2)

printLinkedList(reverseList(head= node1))