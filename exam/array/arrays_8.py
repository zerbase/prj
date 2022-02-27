class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        rtv = False
        for i in range(len(arr)-1):
            for j in range(i +1 , len(arr)):
                if arr[i] == 2 * arr[j]:
                    rtv = True
                if arr[i] * 2 == arr[j]:
                    rtv = True
        return rtv