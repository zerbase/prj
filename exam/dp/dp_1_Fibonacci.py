class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        fl = list(0 for i in range(n+1))
        
        fl[0] = 0
        if n> 0:
            fl[1] = 1
        
        for i in range(2, n+1):
            fl[i] = fl[i - 1] + fl[i - 2]
            
        return fl[n]