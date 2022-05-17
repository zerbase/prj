class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        origin_n = set()
        while n not in origin_n:  
            origin_n.add(n)
            temp = 0
            for i in str(n):
                temp += int(i) ** 2  
            n = temp
      
        if n == 1:
            return True
        else:
            return False