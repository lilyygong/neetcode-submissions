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
            if root.left is None and root.right is None: # we are at a leaf
                if remaining == root.val:
                    return True
                else:
                    return False
            remaining = remaining - root.val
            left_result = dfs(root.left, remaining)
            right_result = dfs(root.right, remaining)
            return left_result or right_result
        return dfs(root, targetSum)