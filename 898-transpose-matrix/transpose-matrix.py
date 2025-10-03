class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        NRO=len(matrix)
        NCO=len(matrix[0])
        NRT=NCO
        NCT=NRO
        matrixT=[]
        for i in range(0,NRT):
            temp=[]
            for j in range(0,NCT):
                temp.append(matrix[j][i])
            matrixT.append(temp)
        return matrixT