    # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
       
        def lv(l, root, rtv):                 
            insertarry(rtv, l)
            rtv[l].append(root.val)
            
            if root.left or root.right:
                l +=1      
            if root.left:
                lv(l, root.left, rtv)
            if root.right:
                lv(l, root.right, rtv)     

        def insertarry(arr, l):
            if len(arr) <= l + 1:
                for i in range(len(arr), l+1):
                    arr.append([])
                    
        rtv = []            
        if root is None:
            return rtv
        
        lv(0, root, rtv)
        
        return rtv 
