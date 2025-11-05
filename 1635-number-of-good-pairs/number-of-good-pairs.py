class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        count=0
        for i in range(0,l):
            for j in range(i+1,l):
                if(nums[i]==nums[j]):
                    count+=1
        return count
