# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, remaining) -> bool:
            if root is None:
                return False
            remaining = remaining - root.val
            if root.left is None and root.right is None and remaining == 0:
                return True
            else:
                left = dfs(root.left, remaining)
                right = dfs(root.right, remaining)
                return left or right

        return dfs(root, targetSum)