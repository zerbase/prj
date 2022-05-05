class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        s
        for ch in s.strip()[0:]:
            if ch == ' ':
                cnt = 0
            else:
                cnt +=1

        return cnt

