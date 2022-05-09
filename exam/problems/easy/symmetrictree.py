# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.check_mirror(root.left, root.right)
        
    def check_mirror(self, p,q):
        if p is None or q is None:
            return p == q
        
        if  p.val != q.val:
            return False
        
        return self.check_mirror(p.left, q.right) and self.check_mirror(p.right, q.left)
        