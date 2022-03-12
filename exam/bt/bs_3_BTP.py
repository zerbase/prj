# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
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
            bs(node.left)
            bs(node.right)
            rtv.append(node.val) 
        
        bs(root)
        
        return rtv
