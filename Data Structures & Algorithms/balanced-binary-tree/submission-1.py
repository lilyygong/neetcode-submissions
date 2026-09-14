# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return (True, 1)
            left_balanced, left_height = dfs(root.left)
            right_balanced, right_height = dfs(root.right)
            if left_balanced and right_balanced and abs(left_height - right_height) <= 1:
                isBalanced = True
                height = max(left_height, right_height) + 1
            else:
                isBalanced = False
                height = max(left_height, right_height) + 1
            return (isBalanced, height)
        isBalanced, _ = dfs(root)
        return isBalanced
