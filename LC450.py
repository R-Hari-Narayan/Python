# Delete node in a BST

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val == key:
            #delete node
            if root.left:
                l = root.left
                rightMost = l
                while rightMost.right:
                    rightMost = rightMost.right
                rightMost.right = root.right
                return root.left
            elif root.right:
                r = root.right
                leftMost = r
                while leftMost.left:
                    leftMost = leftMost.left
                leftMost.left = root.left
                return root.right
            else:
                return None
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
    
def insertNode(root: Optional[TreeNode], val: int)-> TreeNode:
    if not root:
        node = TreeNode(val= val)
        return node
    if (val > root.val):
        root.right = insertNode(root.right, val)
    else:
        root.left = insertNode(root.left, val)
    return root

def printTree(root: Optional[TreeNode]):
    if not root:
        print("Empty")
        return
    q = deque([root])
    while q:
        print()
        size = len(q)
        for _ in range(size):
            node = q.popleft()
            print(node.val, end= " ")
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    
sol = Solution()
nodes = [5,3,6,2,4,7]
root = None
for node in nodes:
    root = insertNode(root, node)
printTree(root= root)
sol.deleteNode(root, 6)
printTree(root)