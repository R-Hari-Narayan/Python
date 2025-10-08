# Binary tree right side view

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root, None])
        output = []
        node = root
        while q:
            prv = node
            node = q.popleft()
            if node!= None:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                continue
            elif ((node == None) and (len(q)> 0)):
                q.append(None)
            output.append(prv.val)
        return output
    

sol = Solution()

node5 = TreeNode(val= 5)
node4 = TreeNode(val= 4)
node3 = TreeNode(val= 3, right= node4)
node2 = TreeNode(val= 2, right= node5)
node1 = TreeNode(val= 1, left= node2, right= node3)

print(sol.rightSideView(root= node1))