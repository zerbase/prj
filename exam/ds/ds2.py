class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = 0
        maxsum = min(nums)
        for i in nums:
            if(maxsum < sums + i):
                maxsum = sums + i
            sums += i
            if sums < 0:
                sums = 0
        return maxsum
    
        
#         end_sum = 0
#         sol = min(nums)

#         for i in nums:
#             end_sum = max(end_sum + i, i)
#             sol = max(end_sum, sol)
#         return sol
