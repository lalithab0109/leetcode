class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        check=0
        for i in range(0,len(nums)-1):
            if(nums[i]<nums[i+1]):
                check=1
                break
            elif(nums[i]>nums[i+1]):
                check=2
                break
        if(check==0):
            return True
        elif(check==1):
            for i in range(0,len(nums)-1):
                if(nums[i]>nums[i+1]):
                    return False
            return True
        else:
            for i in range(0,len(nums)-1):
                if(nums[i]<nums[i+1]):
                    return False
            return True
