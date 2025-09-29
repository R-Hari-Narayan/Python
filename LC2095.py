# Delete the middle node of a linked list
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:
    #Find the middle element position
    ptr = head
    count = 1
    while ptr.next:
        count += 1
        ptr = ptr.next
    print(count)
    if count == 1:
        return None
    middle = int(count/2) if (count % 2 == 0) else int((count-1)/2)

    #Change the next pointer of middle -1 to next of middle element
    ptr1 = head
    for n in range(middle-1):
        ptr1 = ptr1.next
    ptr2 = ptr1.next
    ptr1.next = ptr2.next

    #Delete middle element
    return head

def printLinkedList(head: Optional[ListNode]):
    if head:
        print(head.val)
        printLinkedList(head.next)
    return

node3 = ListNode(val=2)
node2 = ListNode(val=1, next= node3)
node1 = ListNode(val=0, next= node2)
printLinkedList(deleteMiddle(head = node1))