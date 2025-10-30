/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
 #include <stdlib.h>
int* sortedSquares(int* nums, int numsSize, int* returnSize) {
    int *answer;
    answer=(int*)malloc(sizeof(int)*numsSize);
    for(int i=0;i<numsSize;i++){
        answer[i]=nums[i]*nums[i];
    }
    int tmp=0;
    for(int i=0;i<numsSize;i++){
        for(int j=0;j<numsSize-i-1;j++){
            if(answer[j]>answer[j+1]){
                tmp=answer[j];
                answer[j]=answer[j+1];
                answer[j+1]=tmp;
            }
        }
    }
    *returnSize=numsSize;
    return answer;
}