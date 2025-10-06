# Longest zig zag path in a binary tree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maxCount = 0

        def dfs(node):
            if not node:
                return (-1, -1)  # base case, -1 so that +1 becomes 0 for leaf

            left = dfs(node.left)
            right = dfs(node.right)

            # left[1] = longest zigzag if previous move was right
            # right[0] = longest zigzag if previous move was left
            leftZig = 1 + left[1]
            rightZig = 1 + right[0]

            # update global max
            self.maxCount = max(self.maxCount, leftZig, rightZig)

            return (leftZig, rightZig)

        dfs(root)
        return self.maxCount
    

node8 = TreeNode(val= 1)
node7 = TreeNode(val= 1, right= node8)
node6 = TreeNode(val= 1)
node5 = TreeNode(val= 1, right= node7)
node4 = TreeNode(val= 1, left= node5, right= node6)
node3 = TreeNode(val= 1)
node2 = TreeNode(val= 1, left= node3, right= node4)
node1 = TreeNode(val= 1, right= node2)


sol = Solution()
print(sol.longestZigZag(root= node1))