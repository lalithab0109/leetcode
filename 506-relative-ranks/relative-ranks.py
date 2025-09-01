class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        l=len(score)
        i=1
        ranks=score[:]
        scoreTemp=score[:]
        answer=[]

        while(l>0):
            ranks[score.index(max(scoreTemp))]=i
            scoreTemp.remove(max(scoreTemp))
            l=l-1
            i=i+1
        for i in range(0,len(ranks)):
            if ranks[i]==1:
                answer.append("Gold Medal")
            elif ranks[i]==2:
                answer.append("Silver Medal")
            elif ranks[i]==3:
                answer.append("Bronze Medal")
            else:
                answer.append(str(ranks[i]))
        return answer
            



        