class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        sl=sentence.split()
        for i in range(0,len(sl)):
            if str(sl[i][0]).lower() in ["a","e","i","o","u"]:
                sl[i]=str(sl[i])+"ma"
            else:
                sl[i]=str(sl[i][1:])+str(sl[i][0])+"ma"
            sl[i]=str(sl[i])+"a"*(i+1)
        s_new=" ".join(sl)
        return s_new
        