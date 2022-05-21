class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False 
        a1 = []
        a2 = []
        for i in s:
            a1.append(i)
        for i in t:
            a2.append(i)
        
        a1.sort() 
        a2.sort()
        
        for i in range(len(s)):
            if a1[i] != a2[i]:
                return False
        return True