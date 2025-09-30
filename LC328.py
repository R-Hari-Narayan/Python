# Odd Even Linked List

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next or not head.next.next:
        return head
    
    #Store odd head and even head
    oddHead = head
    evenHead = head.next

    #Create three pointer
    ptr = evenHead.next
    oddPtr = oddHead
    evenPtr = evenHead

    while ptr:
        oddPtr.next = ptr
        evenPtr.next = ptr.next
        oddPtr = ptr
        evenPtr = ptr.next
        ptr = ptr.next.next if ptr.next else None

    oddPtr.next = evenHead
    return head
    
def printLinkedList(head: ListNode):
    if head:
        print(head.val)
        printLinkedList(head.next)
    return

node4 = ListNode(4)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
printLinkedList(oddEvenList(head= node1))