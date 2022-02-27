class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in reversed(range(len(nums))):
            if i > 0:
                if nums[i] == nums[i-1]:
                    del nums[i]
            
        
        return len(nums)