class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        sqroot=math.sqrt(area)
        for i in range(int(sqroot),0,-1):
            if(area%i==0):
                W=i
                break
        L=area/W
        return [L,W]


        