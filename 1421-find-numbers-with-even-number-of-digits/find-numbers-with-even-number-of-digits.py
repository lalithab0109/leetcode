class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for i in range(0,len(nums)):
            temp_str=str(nums[i])
            if((len(temp_str))%2==0):
                count+=1
        return count
        