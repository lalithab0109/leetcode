class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        text_l=list(text)
        balloon_l=list("balloon")
        n=len(text)
        count=0
        check=1
        while(n>=len(balloon_l)):
            for i in range(0,len(balloon_l)):
                if balloon_l[i] in text_l:
                    text_l.remove(balloon_l[i])
                else:
                    check=0
                    break
            if(check==1):
                count+=1
                n-=len(balloon_l)
                continue
            else:
                break
        return count
            
                
        