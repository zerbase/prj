class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ar = []
        ar.append(1)
        ar.append(2)
        ar.append(3)
        
        for i in range(3, n):
            ar.append(ar[i-2] + ar[i-1])
        
        return ar[n-1]
    
        
        
