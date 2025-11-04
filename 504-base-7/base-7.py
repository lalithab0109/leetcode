class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans=""
        num_org=num
        num=abs(num)
        if(num==0):
            return "0"
        while(num>0):
            ans+=str((num)%7)
            num=num/7
        if(num_org<0):
            return "-"+ans[::-1]
        else:
            return ans[::-1]
        