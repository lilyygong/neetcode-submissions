# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_sum = root.val
        def dfs(root):
            nonlocal global_sum
            if root is None:
                return 0
            left_sum = dfs(root.left)
            right_sum = dfs(root.right)
            if left_sum < 0:
                left_sum = 0
            elif right_sum < 0:
                right_sum = 0
            curr_sum = max(left_sum, right_sum) + root.val
            temp_sum = left_sum + right_sum + root.val
            global_sum = max(global_sum, temp_sum, curr_sum)
            return curr_sum
        dfs(root)
        return global_sum