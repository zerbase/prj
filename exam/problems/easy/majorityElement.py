class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums) / 2
        count = {}
        for i in nums:
            try: 
                count[i] +=1
            except:
                count[i] = 1
        for i in count:
            if count[i] > nums_len:
                return i