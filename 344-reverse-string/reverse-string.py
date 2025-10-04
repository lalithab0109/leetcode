class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        temp=""
        l=len(s)
        for i in range(0,(len(s)/2)):
            temp=s[i]
            s[i]=s[l-1-i]
            s[l-1-i]=temp
        return s
