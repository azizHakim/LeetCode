# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(node, curmx):
            if not node:
                return
            if node.val>=curmx:
                count[0] += 1
                curmx = node.val
            dfs(node.left, curmx)
            dfs(node.right, curmx)
        count = [0]
        dfs(root, root.val)
        return count[0]
                