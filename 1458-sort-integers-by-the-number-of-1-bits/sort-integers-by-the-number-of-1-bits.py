class Solution(object):
    def count1bits(self,n):
        count=0
        num_org=n
        while(n>0):
            if(n&1==1):
                count+=1
            n=n>>1
        return (count,num_org)
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        output=[]
        for i in range(0,len(arr)):
            output.append(self.count1bits(arr[i]))
        output.sort()
        for i in range(0,len(arr)):
            output[i]=output[i][1]
        return  output
    

        