class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = list(map(lambda x: x**2, nums))
        nums.sort()
        return nums
