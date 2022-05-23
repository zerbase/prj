class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s = s.strip()
        if s == '':
            return 0
        p_s  = ''
        rtv = ''
        for i in s[0:]:
            if i == ' ' and p_s == ' ':
                continue
            rtv += i
            p_s = i
            
            
        return len(rtv.split(' '))