class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        s = list(s)
        s.sort()
        
        if len(s) < 3:
            return s[-1]
        
        else:
            return s[-3]
        
