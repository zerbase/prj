class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = []
        
        l.append(0)
        l.append(1)
        l.append(1)
        
        for i in range(0, n-2): 
            l.append(l[i] + l[i+1] + l[i+2])
        
        return l[n]
        
