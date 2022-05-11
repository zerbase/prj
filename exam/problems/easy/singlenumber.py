class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while len(nums) > 1:
                p = nums.pop(0)
        
                try:
                    nums.remove(p)
                except:
                    return p        
        return nums[0]