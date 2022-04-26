class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        x3 = 'DM'
        x2 = 'LC'
        x1 = 'VX'
        
        s_list = list(s[::-1])
        print(s_list)
        rtv = 0
        lasti = 'aaaaa'
        for i in s_list:   
                
            if i == 'I':
                v = 1
                if lasti in x1:
                    v = v*-1
                rtv += v
            elif i == 'V':
                rtv += 5
            elif i == 'X':
                v = 10
                if lasti in x2:
                    v = v*-1
                rtv += v
            elif i == 'L':
                rtv += 50
            elif i == 'C':
                v = 100
                if lasti in x3:
                    v = v*-1
                rtv += v
                
            elif i == 'D':
                rtv += 500
            elif i == 'M':
                rtv += 1000
            lasti = i 
        return rtv
            
            
        