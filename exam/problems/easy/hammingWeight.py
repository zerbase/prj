class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        str_n = []
        while n > 0 : 
            str_n.append(n % 2)
            n = n // 2
            
        print(str_n)
        cnt = 0
        for i in str_n:
            if i == 1:
                cnt += 1
        return cnt