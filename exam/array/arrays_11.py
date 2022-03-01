class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        l = len(arr)
        cnt = 0
        arr2 = [-1 for i in range(l)]
        while cnt < l-1: 
            arr.pop(0)
            arr2[cnt] = max(arr)
            cnt += 1
        return arr2
