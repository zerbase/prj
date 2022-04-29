class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alist = []
        
        for i in s[0:]:
            if i == '(':
                alist.append(')')
            elif i == '{':
                alist.append('}')
            elif i == '[':
                alist.append(']')
            else:
                if len(alist) == 0:
                    return False
                if i != alist.pop():
                    return False
        if len(alist) != 0:
            return False
        return True
             
                
                

            
        
            
            

           
            