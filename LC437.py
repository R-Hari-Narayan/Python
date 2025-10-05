# Path sum III

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    count = 0
    targetSum = 0
    def customFun(self, root: Optional[TreeNode], sum):
        if not root:
            return
        sum += root.val
        if sum == self.targetSum:
            self.count += 1
        self.customFun(root.left, sum)
        self.customFun(root.right, sum)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.targetSum = targetSum
        def dfs(root: Optional[TreeNode]):
            if not root:
                return
            self.customFun(root, 0)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.count

def printTree(root: TreeNode):
    if not root:
        return
    q = deque([root, None])  # use None instead of 0 for level marker

    while q:
        node = q.popleft()  # ✅ add parentheses
        if node is None:
            print()  # new line for next level
            if q:
                q.append(None)
        else:
            print(node.val, end=" ")  # print values in one line per level
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

node9 = TreeNode(val= 1)
node8 = TreeNode(val= -2)
node7 = TreeNode(val= 3)
node6 = TreeNode(val= 11)
node5 = TreeNode(val= 2, left= None, right= node9)
node4 = TreeNode(val= 3, left= node7, right= node8)
node3 = TreeNode(val= -3, left= None, right= node6)
node2 = TreeNode(val= 5, left= node4, right= node5)
node1 = TreeNode(val= 10, left= node2, right= node3)

sol = Solution()
print(sol.pathSum(root= node1, targetSum= 8))