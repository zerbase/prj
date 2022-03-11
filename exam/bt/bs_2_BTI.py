class Solution(object):
    def inorderTraversal(self, root):
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
            rtv.append(node.val)
            bs(node.right)
        
        bs(root)
        
        return rtv
