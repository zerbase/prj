class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            snum = str(num)
            temp = 0
            for i in snum:
                temp += int(i)
            num = temp
        return num