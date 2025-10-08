class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        
        rmat=[]
        row=[]
        m=len(mat)
        new_mat=[]
        n=len(mat[0])
        temp=0
        for i in range(0,m):
            new_mat.extend(mat[i])

        if((r*c)!=(m*n)):
            return mat
        else:
            for i in range(0,r):
                for j in range(temp,c+temp):
                    row.append(new_mat[j])
                temp=len(row)*(i+1)
                rmat.append(row)
                row=[]
            return rmat
                    




        