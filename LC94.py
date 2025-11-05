# Binary tree inorder traversal

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    
sol = Solution()
node3 = TreeNode(val= 3)
node2 = TreeNode(val= 2, left= node3)
node1 = TreeNode(val= 1, right= node2)
print(sol.inorderTraversal(node1))