class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        n=len(image)
        for i in range(0,n):
            image[i]=image[i][::-1]
        for i in range(0,n):
            for j in range(0,n):
                if(image[i][j]==0):
                    image[i][j]=1
                else:
                    image[i][j]=0
        return image

        