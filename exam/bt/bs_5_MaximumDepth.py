class Solution(object):
    
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
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
            return 0
        
        lv(0, root, rtv)
        
        return len(rtv)
