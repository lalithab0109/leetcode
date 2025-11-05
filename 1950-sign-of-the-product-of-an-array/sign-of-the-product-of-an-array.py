class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        print(nums)
        x=1
        check=0
        for i in range(0,len(nums)):
            if(nums[i]==0):
                return 0
            elif(nums[i]>0):
                check=1
                if(i%2!=0):
                    x=-1
                    break
                else:
                    x=1
                    break
        if(check==0):
            return -1
        else:
            return x

        