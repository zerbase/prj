class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        end_sum = 0
        sol = min(nums)

        for i in nums:
            end_sum = max(end_sum + i, i)
            sol = max(end_sum, sol)
        return sol
        