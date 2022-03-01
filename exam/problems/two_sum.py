class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        cnt = 0 
        l = len(nums)
        while cnt < l:
            a = nums[0]
            nums.pop(0)
            b = -1
            try: 
                b = nums.index(target - a)
            except:
                pass
            if b > -1:
                return [cnt,cnt + b +1]
            cnt +=1
    
                
~
