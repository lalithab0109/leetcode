class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        var=-1
        ind=[]
        s_set=set(s)
        s_list=list(s_set)
        for i in range(0,len(s_list)):
            if s.count(s_list[i])==1:
                ind.append(s.index(s_list[i]))
                var=1
        if var==-1:
            return var
        else:
            return (min(ind))
        