class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """  
        num_str = ''
        for i in digits:
             num_str += str(i)
        rtv = []
        for i in str(int(num_str) + 1):
            rtv.append(i)
        return rtv