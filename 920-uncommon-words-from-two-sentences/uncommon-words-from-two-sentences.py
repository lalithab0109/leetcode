class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        uncstr=[]
        ls1=s1.split()
        ls2=s2.split()
        for i in range(0,len(ls1)):
            if ls1[i] not in ls2 and ls1.count(ls1[i])==1:
                uncstr.append(ls1[i])
        for i in range(0,len(ls2)):
            if ls2[i] not in ls1 and ls2.count(ls2[i])==1:
                uncstr.append(ls2[i])
        return list(set(uncstr))

        