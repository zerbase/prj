class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        cnt = 1
        while True:
            raw = cnt * cnt 
            if raw > x:
                break
            cnt +=1
        return cnt-1
        