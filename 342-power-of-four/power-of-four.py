class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        import math
        if(n<=0):
            return False
        else:
            x=math.log(n,4)
            pow=math.ceil(x)
            if((4**pow)==n):
                return True
            else:
                return False
        