class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        len_op=len(operations)
        record=[]
        for i in range(0,len_op):
            if(operations[i]=="C"):
                record.pop(len(record)-1)
                
            elif(operations[i]=="D"):
                record.append(2*int(record[len(record)-1]))

            elif(operations[i]=="+"):
                record.append(int(record[len(record)-1])+int(record[len(record)-2]))
            
            else:
                record.append(int(operations[i]))
        return sum(record)

        