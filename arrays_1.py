class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        max_cnt = 0
        for i in nums[0:]:
            if i == 1:
                cnt += 1
                if max_cnt < cnt:
                    max_cnt = cnt            
            else:
                cnt = 0
        return max_cnt