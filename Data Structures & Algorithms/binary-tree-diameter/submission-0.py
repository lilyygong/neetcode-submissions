from math import inf
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDia = 0
        def dfs(root, maxHeight) -> int:
            nonlocal maxDia
            if root is None:
                return 0
            left = dfs(root.left, maxHeight)
            right = dfs(root.right, maxHeight)
            maxDia = max(maxDia, (left + right))
            return max(left, right) + 1
        dfs(root, -inf)
        return maxDia