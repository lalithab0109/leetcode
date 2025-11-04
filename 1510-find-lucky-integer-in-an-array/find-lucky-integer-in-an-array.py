class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        lucky_nos=[]
        for i in range(0,len(arr)):
            if arr[i]==arr.count(arr[i]):
                lucky_nos.append(arr[i])
        if(len(lucky_nos)!=0):
            return max(lucky_nos)
        else:
            return -1
        