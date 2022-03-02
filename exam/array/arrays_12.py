class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        cnt = 0
        i = 0 
        while cnt < len(nums):
            a = nums[i]
            nums.pop(i)
            if a == 0:
                nums.append(a)
            else: 
                nums.insert(i, a)
                i += 1
            cnt += 1
