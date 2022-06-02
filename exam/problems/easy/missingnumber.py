class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        le = len(nums)
        # nums.sort()
        for i in range(le+1):
            if i not in nums:
                return i