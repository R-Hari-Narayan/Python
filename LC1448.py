# Count good nodes in a binary tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    count = 0
    def customFunc(self, root: TreeNode, max: int):
        if not root:
            return
        if root.val >= max:
            max = root.val
            self.count += 1
        self.customFunc(root= root.left, max= max)
        self.customFunc(root= root.right, max= max)

    def goodNodes(self, root: TreeNode) -> int:
        self.customFunc(root= root, max= root.val) 
        return self.count

def printTree(root: TreeNode):
    if root:
        print(root.val)
        printTree(root.left)
        printTree(root.right)

node6 = TreeNode(val=5)
node5 = TreeNode(val=1)
node4 = TreeNode(val=3)
node3 = TreeNode(val=4, left= node5, right= node6)
node2 = TreeNode(val=1, left= node4)
node1 = TreeNode(val=3, left= node2, right= node3)

#printTree(root=node1)

sol = Solution()
print(sol.goodNodes(root=node1))