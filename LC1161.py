# Maximum level sum of a binary tree

from typing import Optional
from collections import deque
import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxLevel = 1
        maxSum = -sys.maxsize
        q= deque([root, None])
        sum = 0
        level = 1
        while q:
            node = q.popleft()
            if node is None:
                if sum > maxSum:
                    maxSum = sum
                    maxLevel = level
                level += 1
                sum = 0
                if q:
                    q.append(None)
                
            else:
                sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
        return maxLevel
    

node3 = TreeNode(val= 3)
node2 = TreeNode(val= 2)
node1 = TreeNode(val= 1, left= node2, right= node3)

sol = Solution()
print(sol.maxLevelSum(root= node1))