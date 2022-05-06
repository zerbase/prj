class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        cnt = 0
        bsum = 0
        for i in a[::-1]:
            bsum += int(i) * (2 ** cnt)
            cnt += 1
        cnt = 0
        for i in b[::-1]:
            bsum += int(i) * (2 ** cnt)
            cnt +=1
            
        rtv = []
        while bsum > 0:
            a = bsum % 2
            rtv.append(a)
            bsum = bsum // 2 
        r = ''
        for i in rtv[::-1]:
            r += str(i)
            
        if r == '':
            return '0'
        return r