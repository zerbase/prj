class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        rtv = []
        num_cnt = dict(Counter(nums1))
        
        for i in nums2:
            if i in num_cnt and num_cnt[i] !=0:
                rtv.append(i)
                num_cnt[i] = num_cnt[i] -1
        return rtv