class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        st = set(nums)
        if len(st) != len(nums):
            return True
        else:
            return False