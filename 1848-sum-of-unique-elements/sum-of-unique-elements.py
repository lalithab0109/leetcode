class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_unique=list(set(nums))
        sum_uni=0
        for i in range(0,len(nums_unique)):
            if(nums.count(nums_unique[i])==1):
                sum_uni+=nums_unique[i]
        return sum_uni
        