/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

int* countBits(int n, int* returnSize) {
    int *ans;
    ans=malloc(sizeof(int)*(n+1));
     int num_of_1s(int num){
        int count=0;
        while(num>0){
            if(num&1) count++;
            num=num>>1;
        }
        return count;
    }
    for(int i=0;i<n+1;i++){
        
        ans[i]=num_of_1s(i);
    }
    *returnSize=n+1;
    return ans;

    
}