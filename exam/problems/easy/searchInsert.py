class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        cnt = 0
        for i in nums:
            if i >= target:
                nums.insert(cnt, target)
                break
            cnt += 1
        return cnt
        
        