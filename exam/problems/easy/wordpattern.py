class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split(' ')
        
        temp = {}
        
        if len(s) != len(pattern):
            return False
        
        if len(set(s)) != len(set(pattern)):
            return False
        
        for i in range(len(s)):
            if pattern[i] not in temp:
                temp[pattern[i]] = s[i]
            else:
                if s[i] != temp[pattern[i]]:
                    return False
        return True