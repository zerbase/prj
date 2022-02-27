class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even_cnt = 0
        for i in nums[0:]:
            par = 0
            while i > 0:
                i = i/10
                par += 1
            if par%2 == 0:
                even_cnt += 1
        return even_cnt