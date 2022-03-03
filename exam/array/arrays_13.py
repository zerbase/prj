class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        s = heights[:]
        s.sort()
        cnt = 0
        for i in range(len(s)):
            if s[i] != heights[i]:
                cnt += 1
        return cnt
