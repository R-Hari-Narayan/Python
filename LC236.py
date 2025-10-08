# Lowest common ancestor of a binary tree
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val, left= None, right= None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        
        l= self.lowestCommonAncestor(root.left, p, q)
        r= self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        else:
            return l or r
    
node9 = TreeNode(val = 4)
node8 = TreeNode(val = 7)
node7 = TreeNode(val = 8)
node6 = TreeNode(val = 0)
node5 = TreeNode(val = 2, left= node8, right= node9)
node4 = TreeNode(val = 6)
node3 = TreeNode(val = 1, left= node6, right= node7)
node2 = TreeNode(val = 5, left= node4, right= node5)
node1 = TreeNode(val = 3, left= node2, right= node3)

sol = Solution()
ans = sol.lowestCommonAncestor(root= node1, p= node2, q= node3)
print(ans.val)