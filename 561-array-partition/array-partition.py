class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsD=sorted(nums,reverse=True)
        sum_max=0
        for i in range(0,len(numsD)-1,2):
            sum_max=sum_max+min(numsD[i],numsD[i+1])
        return sum_max


