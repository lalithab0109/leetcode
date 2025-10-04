class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        l=len(columnTitle)
        column_no=0
        for i in range(0,l):
            column_no+=(ord(columnTitle[l-1-i])-64)*(26**i)
        
        return column_no
        
        