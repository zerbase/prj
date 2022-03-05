class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rtv = []
        for i in range(len(nums)):
            rtv.append(i+1)
        rtv = list(set(rtv) - set(nums))
                
        return rtv
