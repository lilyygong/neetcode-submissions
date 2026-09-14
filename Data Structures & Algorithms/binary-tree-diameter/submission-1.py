# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia = 0
        def dfs(root):
            nonlocal dia
            if root is None:
                return 0
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            curr_height = max(left_height, right_height) + 1
            dia = max(dia, left_height + right_height)
            return curr_height
        dfs(root)
        return dia