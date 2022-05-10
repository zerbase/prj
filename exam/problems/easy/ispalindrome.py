class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        text = re.sub('[^a-zA-Z0-9]',' ',s).strip()
        text = text.replace(' ', '')
        text = text.lower()
        if len(text) < 2:
            return True
        for i in range((len(text)//2)):
            if text[i] != text[-(i+1)]:
                return False
        return True
        