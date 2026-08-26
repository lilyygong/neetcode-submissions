# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        root_nodes = []
        subroot_nodes = []
        def dfs_root(root):
            if root is None:
                root_nodes.append(None)
                return 
            root_nodes.append(root.val)
            dfs_root(root.left)
            dfs_root(root.right)
        def dfs_subroot(subroot):
            if subroot is None:
                subroot_nodes.append(None)
                return 
            subroot_nodes.append(subroot.val)
            dfs_subroot(subroot.left)
            dfs_subroot(subroot.right)
        dfs_root(root)
        dfs_subroot(subRoot)
        if root_nodes == subroot_nodes:
            return True
        elif len(subroot_nodes) > len(root_nodes):
            return False
        left, right = 0, len(subroot_nodes) - 1
        for i in range(len(root_nodes)):
            curr_window = root_nodes[left:right + 1]
            if curr_window == subroot_nodes:
                return True
            left += 1
            right += 1
        return False
        