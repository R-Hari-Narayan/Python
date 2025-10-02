# Maximum depth of a binary tree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    l = maxDepth(root.left)
    r= maxDepth(root.right)
    return 1 + max(l,r)

def dfs(node: Optional[TreeNode]):
    if not node:
        return
    print(node.val)
    dfs(node.left)
    dfs(node.right)

node4 = TreeNode(val=4)
node3 = TreeNode(val=3)
node2 = TreeNode(val=2, left= node4)
node1 = TreeNode(val=1, left= node2, right= node3)
print(maxDepth(node1))