class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False
        if arr[1] < arr[0]:
            return False
        t_max = 0
        tt = False
        for i in range(0,len(arr)-1) :

            # if i == 0:
            #     if arr[i+1] < arr[i]:
            #         return False
            if arr[i+1] == arr[i]:
                return False 
            if arr[i+1] > arr[i]:
                if tt and t_max != 0:
                    return False
                t_max = arr[i+1]                
            if arr[i+1] < arr[i]:
                tt = True
                    
        if tt:
            return True
        else :
            return False