class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans=[]
        val1=0
        val2=0
        index1=0
        index2=0
        unique_nums=list(set(numbers))
        unique_nums=sorted(unique_nums)
        for i in range(0,len(unique_nums)):
            val1=unique_nums[i]
            index1=numbers.index(unique_nums[i])
            val2=target-val1
            if(val2 in unique_nums):
                numbers.pop(numbers.index(val1))
                index2 = numbers.index(val2)
                break
        return [index1+1,index2+2]
        
            
        
                
        