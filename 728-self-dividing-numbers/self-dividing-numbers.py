class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        answer=[]
        for num in range(left,right+1):
            numOrg=num
            while(num>0):
                digit=num%10
                if(digit==0 or numOrg%digit!=0):
                    break
                num=num/10
            if num==0:
                answer.append(numOrg)
            num=numOrg
        return answer

                
            
            
    
        