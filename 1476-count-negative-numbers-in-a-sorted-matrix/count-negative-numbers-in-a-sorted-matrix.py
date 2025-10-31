class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        flat_mat=[]
        for i in range(0,len(grid)):
            flat_mat.extend(grid[i])
        flat_mat=sorted(flat_mat)
        count=0
        for i in range(0,len(flat_mat)):
            if(flat_mat[i]>0 or flat_mat[i]==0):
                break
            else:
                count+=1
        return count

        