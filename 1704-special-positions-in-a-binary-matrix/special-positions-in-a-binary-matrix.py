class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m=len(mat)
        n=len(mat[0])
        col=[]
        mat_col=[]
        count=0
        for j in range(0,n):
            for i in range(0,m):
                col.append(mat[i][j])
            mat_col.append(col)
            col=[]
        print(mat_col)
        for i in range(0,m):
            for j in range(0,n):
                if (mat[i][j]==1 and sum(mat_col[j])==1 and sum(mat[i])==1):
                    count+=1
        return count

        