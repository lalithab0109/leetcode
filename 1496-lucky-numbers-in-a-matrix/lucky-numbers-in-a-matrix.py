class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        min_ele=[]
        min_index=[]
        columns=[]
        for i in range(0,len(matrix)):
            min_ele.append(min(matrix[i]))
            min_index.append(matrix[i].index(min(matrix[i])))   
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix)):
                columns.append(matrix[j][min_index[i]])
            if(min_ele[i]==max(columns)):
                return [min_ele[i]]
            columns=[]
        return []
        