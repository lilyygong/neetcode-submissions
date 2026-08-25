# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#recurse both trees, put them into arrays, compare the arrays
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_arr = []
        q_arr = []
        def dfs_p(p):
            if p is None:
                p_arr.append(None)
                return
            p_arr.append(p.val)
            left = dfs_p(p.left)
            right = dfs_p(p.right)
        def dfs_q(q):
            if q is None:
                q_arr.append(None)
                return
            q_arr.append(q.val)
            left = dfs_q(q.left)
            right = dfs_q(q.right)
        dfs_p(p)
        dfs_q(q)
        return p_arr == q_arr