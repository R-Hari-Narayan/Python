# Search in a Binary Search Tree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
    
node5 = TreeNode(val = 3)
node4 = TreeNode(val = 1)
node3 = TreeNode(val = 7)
node2 = TreeNode(val = 2, left= node4, right= node5)
node1 = TreeNode(val = 4, left= node2, right= node3)

sol = Solution()
ans = sol.searchBST(root= node1, val= 2)
print(ans.val)