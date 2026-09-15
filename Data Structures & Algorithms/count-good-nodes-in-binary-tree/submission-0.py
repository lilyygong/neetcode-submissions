# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = 0 # root is always good
        def dfs(root, maxParent):
            nonlocal goodNodes
            if root is None:
                return None
            if root.val >= maxParent:
                goodNodes += 1
            maxParent = max(root.val, maxParent)
            dfs(root.left, maxParent)
            dfs(root.right, maxParent)
        
        dfs(root, root.val)
        return goodNodes