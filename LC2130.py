# Maximum twin sum of a linked list

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def pairSum(head: Optional[ListNode]) -> int:
    lst = []
    while head:
        lst.append(head.val)
        head= head.next
    l = 0
    r = len(lst)-1
    largest = 0
    while l< r:
        if lst[l] + lst[r] > largest:
            largest = lst[l] + lst[r]
        l+= 1
        r-= 1
    return largest


def printLinkedList(head: ListNode):
    if head:
        print(head.val)
        printLinkedList(head.next)

node4 = ListNode(val= 4)
node3 = ListNode(val= 2, next= node4)
node2 = ListNode(val= 2, next= node3)
node1 = ListNode(val= 3, next= node2)
print(pairSum(head=node1))