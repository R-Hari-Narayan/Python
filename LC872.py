# Leaf similar trees

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafNodes(self, node: TreeNode):
        if not node:
            return []
        leafSqn = []
        if not node.left and not node.right:
            leafSqn.append(node.val)
            return leafSqn
        leafSqn += self.leafNodes(node.left)
        leafSqn += self.leafNodes(node.right)
        return leafSqn
    
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        L1 = self.leafNodes(root1)
        L2 = self.leafNodes(root2)
        return L1 == L2
    
node4 = TreeNode(val=4)
node3 = TreeNode(val=3, left= node4)
node2 = TreeNode(val=2)
node1 = TreeNode(val=1, left= node2, right= node3)
sol = Solution()
print(sol.leafNodes(node= node1))
