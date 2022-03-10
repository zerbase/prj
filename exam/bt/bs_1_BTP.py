# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rtv = []
        
        if not root:
            return rtv
        
        def bs(node):
            if not node: 
                return []
            rtv.append(node.val)
            bs(node.left)
            bs(node.right)
        
        bs(root)
        
        return rtv
