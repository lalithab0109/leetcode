class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        answer=[]
        if n%2==0:
            for i in range(1,(n+2)/2):
                answer.append(i)
                answer.append(-i)
            return answer
        else:
            answer.append(0)
            for i in range(1,(n+1)/2):
                answer.append(i)
                answer.append(-i)
            return answer
        