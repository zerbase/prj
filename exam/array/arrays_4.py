class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        temp = arr[:]
        flag = True
        for i in range(0,len(arr)-1):
            if arr[i] == 0 and flag:
                arr[i+1] = 0
                for j in range(i+2,len(arr)):
                    arr[j] = temp[j-1]
                temp = arr[:]
                flag = False
            else:
                flag = True

        return arr