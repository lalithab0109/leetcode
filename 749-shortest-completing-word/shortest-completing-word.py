class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        temp=""
        for i in range(0,len(words)-1):
            for j in range(0,len(words)-i-1):
                if(len(words[j])>len(words[j+1])):
                    temp=words[j]
                    words[j]=words[j+1]
                    words[j+1]=temp
        lp=licensePlate.lower()
        str_lp=""
        check=1
        for i in range(0,len(lp)):
            if(lp[i]>='a'and lp[i]<='z'):
                str_lp+=lp[i]
        print(str_lp)
        for i in range(0,len(words)):
            for j in range(0,len(str_lp)):
                if(words[i].count(str_lp[j])<str_lp.count(str_lp[j])):
                    check=0
                    break
            if(check==1):
                return words[i]
            check=1



        