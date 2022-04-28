class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i = 0
        bp = False
        sd = strs[0]
        while True:
            for st in strs:
                if len(st) < i+1:
                    bp =True
                    break
                if sd[i] != st[i]:
                    bp = True  
                    break
            if bp:
                return sd[0:i]
            i += 1