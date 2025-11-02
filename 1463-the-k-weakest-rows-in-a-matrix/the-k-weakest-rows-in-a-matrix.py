class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        no_of_sold=[]
        no_of_sold_index=[]
        for i in range(0,len(mat)):
            no_of_sold.append(sum(mat[i]))
        max_no_of_sold=max(no_of_sold)
        for i in range(0,k):
            no_of_sold_index.append(no_of_sold.index(min(no_of_sold)))
            no_of_sold[no_of_sold.index(min(no_of_sold))]=max_no_of_sold+1
        return no_of_sold_index
        